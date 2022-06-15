# Epmwebapi Library

Developed by **Elipse Software**, the **Epmwebapi** library allows for interaction with data from your **Elipse Plant Manager (EPM)** platform. 
It gives you greater flexibility to search, organize, analyze, share, and monitor data from the industrial process.

It is commonly used for, but not limited to, generating indicators, data analysis, statistics, and intelligence processes geared at industrial systems such as 
Chemical and Petrochemical Industries, Pulp and Paper, Steel, Energy, Water and Wastewater, Data Centers, Smart Buildings, among others.

For further information about **EPM**, check out https://www.elipse.com.br/produto/elipse-plant-manager/

**Requirements:**
* EPM Webserver 3.06 (for accessing data from EPM Server; it doesn’t need to be installed in the same device as epmwebapi).
* Python 3.6 x64 or higher

**Installation:**

Online (recommended): 
* After installing Python, go to the command prompt or terminal and type: pip install epmwebapi. The installer will proceed to download and install the library and its add ons.
 
Offline: 
* Download the product via [Elipse's website](https://www.elipse.com.br/en/downloads/)
* Decompress the **epmwebapi** folder and copy it to the site-packages directory at Python. 
* Install the following add ons: Numpy Libraries, Requests, and Python-dateutil.

**Note: Sometimes Github is not able to show the examples below. I case of error, use one of the alternate links below:**

[NBViewer](https://nbviewer.jupyter.org/github/elipsesoftware/epmwebapi/tree/master/exemplos/) - Jupyter’s notebooks viewer

[EPMTR](http://epmtr.elipse.com.br/repoepmwebapi) - Examples in HTML at Elipse’s server

**In case you can’t visualize any of these examples, send an e-mail to supportepm@elipse.com.br**

**Examples:**

* [Basic example](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/Quickstart.ipynb) - Examples of data write and read, as well as notes.
* [Matplotlib](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_matplotlib.ipynb) - Use this library to generate charts.
* [Pandas](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_pandas.ipynb) - Use this library to generate charts.
* [Pandas and dataviz](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/pandas_and_dataviz.ipynb) - Use these libraries to handle data and generate graphic visualizations.
* [Numpy](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_numpy.ipynb) - Numpy is an essential library to work with data calculations in matrices.
* [Regression by decision tree](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/decision_tree_regression.ipynb) - Use the Scikit-learn library to make a regression.
* [Using concurrence](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/concorrencia_historyReadAggregate.ipynb) - Use concurrence for high-performance queries to EPM Server.
* [Retrieving a webserver and writing at EPM Server](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/write_from_webserver.ipynb) - Reading temperature data from INPE’s webserver and writing a variable from EPM Server.
* [Machine Learning](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_machine_learning.ipynb) - General concepts and examples of this technique widely used for process data.
* [Temperature and thermal comfort analysis](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/temp_elipse_ecc.ipynb) - Analysis of real data from Elipse Software facilities.
* [Generating maps](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/maps.ipynb) - Working with geolocation and interactive maps data.
* [Accessing information from EPM Server](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/server_information.ipynb) - Accessing data such as version, hardware/softkey, Interface Servers diagnosis, etc.
* [Improving performance in historyReadRaw queries](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/concorrencia_historyReadRaw.ipynb) - Working with concurrent.futures module for Raw queries, with potential improved performance especially when several variables are being researched.
* [Improving performance in historyReadAggregate queries](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/concorrencia_historyReadAggregate.ipynb) - Working with concurrent.futures module for Aggregate queries, with potential improved performance especially when several variables are being researched.
* [Retrieving data from Communication Interfaces](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/int_svr_status.ipynb) - Information from communication interfaces (EPM Interfaces).
* [Example of 3D and polar charts](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/matplotlib_3d_polar.ipynb) - How to make 3D and polar charts with data from the process.
* [Reading data from TXT, CSV, XLSX and JSON files](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/reading_from_file.ipynb) - How to read data from different types of files (TXT, CSV, XLSX and JSON).
* [Reading data from the process and converting to Pandas's DataFrame](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/sample01.ipynb) - reading data from EPM Server’s process (OPC UA Server), creating a DataFrame from Pandas’s module, and examples of analyses.
* [Thermal comfort analysis ](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/sample02.ipynb) - reading data from EPM Server’s process (OPC UA Server), creating a DataFrame from Pandas’s module, and thermal comfort analysis ([Webinar - Data analysis with Python and Dashboard Web](https://youtu.be/IYg5yutkIhw)).
* [Generating reports in HTML and/or PDF](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/PdfReport_Temperatures.ipynb) - Generating reports in HTML or PDF, addressing questions about Jinja2, Base64, reading information from ambient variables, creating time series with Pandas converting UTC to local time.
* [CRUD in Basic Variables](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basicvariables_CRUD.ipynb) - Creating, reading, updating, and deleting Basic Variables from EPM Server.










