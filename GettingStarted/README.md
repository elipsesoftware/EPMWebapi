# Getting started

## Installation

Epmwebapi is installed as part of the [EPM Processor](https://github.com/elipsesoftware/EPMProcessor). So if you are using with it, there is no need to do the manual installation.

But you can use it independently, acoording to your need. 
Then Epmwebapi can be installed via pip from [PyPI](https://pypi.org/project/epmwebapi/):

`pip install epmwebapi`



### Installing with Anaconda
In Anaconda is recomended to create a virtual environment: 

Run `conda create -v venv_name`

And `source activate venv_name`

Where `venv_name` is the name of your virtual environment.

Run `conda install pip` this will install pip to your venv directory.

Install epmwebapi running `/anaconda/envs/venv_name/bin/pip install epmwebapi`

## Python version support
Python 3.6 and 3.7. 

## Overview

Epmwebapi is a Python package that allows interaction with the [Elipse Plant Manager](https://www.elipse.com.br/en/produto/elipse-plant-manager/) platform. 

Some possibilities that the package offers are:

* Historical and real-time queries 
* Write values to EPM Variables
* Interact with EPM Portal and EPM Processor resources
* CRUD of Basic Variables
* Build and edit CustomTypes and EPMModel
* Read, edit and create EPM Studio Datasets 

## Quickstart

Import library

```python
import epmwebapi as epm
```
Create connection to an EPMWebServer available address. In this example  the EPMWebServer are installed in the same machine of the running code, and configured with default 44333 and 44332 ports
```python
connection = epm.epm.EpmConnection('http://localhost:44333', 'http://address:44332', 'user', 'password')
```

Reading raw data

```python
#variable name
variable_name = 'Temperature'

#method to get the variable
bv = connection.getDataObjects([variable_name])

#define query period
import datetime
end_date = datetime.datetime.now()
ini_date= end_date - datetime.timedelta(minutes=10)
queryPeriod = epm.QueryPeriod(ini_date,end_date)

#make read
data = bv[variable_name].historyReadRaw(queryPeriod)
```
The return of historyReadRaw is a Numpy ndarray time series with this format:

|Value|Timestamp|Quality|
|---|---|---|
|0.12| datetime.datetime(2019, 12, 11, 15, 37, 59, 554738, tzinfo=datetime.timezone.utc)| 0
|1.45| datetime.datetime(2019, 12, 11, 15, 45, 59, 554738, tzinfo=datetime.timezone.utc)| 0
|5.00| datetime.datetime(2019, 12, 11, 15, 49, 59, 554738, tzinfo=datetime.timezone.utc)| 0
|2.48| datetime.datetime(2019, 12, 11, 16, 7, 59, 554738, tzinfo=datetime.timezone.utc)| 0
|6.00| datetime.datetime(2019, 12, 11, 16, 20, 59, 554738, tzinfo=datetime.timezone.utc)| 0

For more information take a look at the User Guide and the API Reference.
