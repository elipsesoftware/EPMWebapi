# Epmwebapi Library

Developed by **Elipse Software**, the **Epmwebapi** library allows interaction with data from your **Elipse Plant Manager (EPM)** platform. It provides flexibility to search, organize, analyze, share, and monitor industrial process data.

Its typical, but not exclusive, use is the generation of indicators, data analysis, statistics, and process intelligence for industrial systems, such as:
* Chemical Industry;
* Petrochemical;
* Pulp and Paper;
* Steelmaking;
* Energy;
* Sanitation;
* Data Center Infrastructure Management (DCIM);
* Smart Buildings;
* Others.

More information about **EPM** can be found on the website [https://www.elipse.com.br/en/produto/elipse-plant-manager/](https://www.elipse.com.br/en/produto/elipse-plant-manager/)

**Requirements:**
* Python 3.10 (x64) or higher, lower than 3.14.

**Installation:**

Online (Recommended):
* After installing Python, open the command prompt or terminal and type the following command: *pip install epmwebapi*. The installer will take care of downloading and installing the library and its dependencies.

Offline:
* Download the package from the [PyPI](https://pypi.org/project/epmwebapi/#description) website.
* Unzip the **epmwebapi** folder and copy it to the **site-packages** directory of your Python installation.
* Install dependencies: Numpy, Requests, and Python-dateutil libraries.

**Examples:**

* [Basic example](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/Quickstart.ipynb) - Examples of data and annotation readings and writings.
* [Matplotlib](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_matplotlib.ipynb) - Using this library to generate graphs.
* [Pandas](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_pandas.ipynb) - Use Pandas to manipulate tabular data.
* [Pandas and dataviz](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/pandas_and_dataviz.ipynb) - Using these libraries to manipulate data and generate graphical visualizations.
* [Numpy](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_numpy.ipynb) - Numpy is an essential library for working with data calculations in arrays.
* [Decision tree regression](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/decision_tree_regression.ipynb) - See how to use the Scikit-learn library to perform regression.
* [Using Concurrency](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/concorrencia_historyReadAggregate.ipynb) - Using concurrency for high-performance queries to the EPM Server.
* [Searching a webserver and writing to EPM Server](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/write_from_webserver.ipynb) - Reading temperature data from the INPE Webserver and writing it to an EPM Server variable.
* [Machine Learning](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_machine_learning.ipynb) - Concepts and examples of using this increasingly common technique in process data.
* [Temperature and thermal comfort analysis](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/temp_elipse_ecc.ipynb) - Analysis of real temperature data from Elipse's rooms.
* [Creating maps](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/maps.ipynb) - Working with geolocation data and interactive maps.
* [Accessing EPM Server information](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/server_information.ipynb) - Accessing information such as version, product key, Interface Server diagnostics, etc.
* [Improving performance in historyReadRaw queries](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/concorrencia_historyReadRaw.ipynb) - Working with the *concurrent.futures* module to perform *Raw* queries, bringing possible performance gains, especially when many variables need to be searched.
* [Improving performance in historyReadAggregate queries](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/concorrencia_historyReadAggregate.ipynb) - Working with the *concurrent.futures* module to perform *Aggregate* queries, bringing possible performance gains, especially when many variables need to be searched.
* [Searching for Communication Interface information](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/int_svr_status.ipynb) - Checking information on communication interfaces (EPM Interfaces).
* [3D and polar graph example](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/matplotlib_3d_polar.ipynb) - Example of how to create a 3D and polar graph with process data.
* [Reading data from TXT, CSV, XLSX, and JSON files](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/reading_from_file.ipynb) - Examples of reading data from various file types (TXT, CSV, XLSX, and JSON).
* [Reading process data and converting to Pandas DataFrame](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/sample01.ipynb) - Reading process data from EPM Server (OPC UA Server), creating a Pandas DataFrame, and examples of analysis.
* [Thermal comfort analysis](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/sample02.ipynb) - Reading process data from EPM Server (OPC UA Server), creating a Pandas DataFrame, and thermal comfort analysis ([Webinar - Data Analysis with Python and Web Dashboard](https://youtu.be/IYg5yutkIhw)).
* [Generating HTML and/or PDF reports](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/PdfReport_Temperatures.ipynb) - Generating HTML or PDF reports, covering topics such as Jinja2, Base64, reading environment variable information, creating time series in Pandas, and converting UTC to local time.
* [CRUD on Basic Variables](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basicvariables_CRUD.ipynb) - Creating, changing configurations, and deleting Basic Variables from EPM Server.
