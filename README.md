# Biblioteca Epmwebapi [<sup><sup><sup>(en-us)</sup></sup></sup>](https://github.com/elipsesoftware/EPMWebapi/blob/master/readme_us.md)

Desenvolvida pela **Elipse Software**, a biblioteca **Epmwebapi** permite a interação com os dados da sua plataforma 
**Elipse Plant Manager(EPM)**. Ela possibilita flexibilidade para buscar, organizar, analisar, compartilhar e monitorar os dados dos processos industriais.

Seu uso típico, mas não exclusivo, é a geração de indicadores, análises de dados, estatísticas e inteligência de processo voltados para sistemas industriais, como:
* Indústria Química;
* Petroquímica;
* Papel e Celulose;
* Siderúrgica;
* Energia;
* Saneamento;
* Gerenciamento de Infraestrutura de Centros de Dados (DCIM);
* Prédios Inteligentes;
* Outros.

Mais informações sobre o **EPM** podem ser encontradas no site https://www.elipse.com.br/produto/elipse-plant-manager/

**Requisitos:**
* Python 3.10 (x64) ou superior, inferior à 3.14.

**Instalação:**

Online (Recomendado):
* Após instalar o Python, abra o prompt de comando ou terminal e digite o seguinte comando: *pip install epmwebapi*. O instalador se encarregará de baixar e instalar a biblioteca e suas dependências.
 
Offline: 
* Faça do download do pacote através do site [PyPI](https://pypi.org/project/epmwebapi/#description).
* Faça a descompactação da pasta **epmwebapi** e copie para o diretório **site-packages** da instalação do Python.
* Instale as dependências: Bibliotecas Numpy, Requests e Python-dateutil.

**Exemplos:**

* [Exemplo básico](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/Quickstart.ipynb) - Exemplos de leituras e escritas de dados e anotações. 
* [Matplotlib](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_matplotlib.ipynb) - Utilizando essa biblioteca para gerar gráficos.
* [Pandas](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_pandas.ipynb) - Use Pandas para manipular dados tabulares.
* [Pandas e dataviz](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/pandas_and_dataviz.ipynb) - Utilizando essas bibliotecar para manipular dados e gerar visualizções gráficas.
* [Numpy](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_numpy.ipynb) - Numpy é uma biblioteca essecial para trabalhar com cálculos de dados em matrizes.
* [Regressão por árvore de decisão](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/decision_tree_regression.ipynb) - Veja como utilizar a biblioteca Scikit-learn para fazer uma regressão. 
* [Utilizando Concorrência](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/concorrencia_historyReadAggregate.ipynb) - Usando concorrência para alta performance de consultas ao EPM Server.
* [Buscando em um webserver e escrevendo no EPM Server](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/write_from_webserver.ipynb) - Lendo dados de temperatura do Webserver do INPE e escrevendo em uma variável do EPM Server. 
* [Machine Learning](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basic_use_machine_learning.ipynb) - Noções e exemplos de uso dessa técnica cada vez mais utilizada em dados de processo.
* [Análise de temperatura e conforto térmico](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/temp_elipse_ecc.ipynb) - Análises de dados reais de temperaturas das salas da Elipse.
* [Criando mapas](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/maps.ipynb) - Trabalhando com dados de geolocalização e mapas interativos. 
* [Acessando informações do EPM Server](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/server_information.ipynb) - Acessando informações como versão, chave de produto, diagnósticos dos Interface Servers, etc. 
* [Melhorando desempenho em consultas historyReadRaw](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/concorrencia_historyReadRaw.ipynb) - Trabalhando com o módulo *concurrent.futures* para fazer consultas *Raw*, trazendo possíveis ganhos de desempenho, principalmente quando se tem muitas variáveis a serem pesquisadas.
* [Melhorando desempenho em consultas historyReadAggregate](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/concorrencia_historyReadAggregate.ipynb) - Trabalhando com o módulo *concurrent.futures* para fazer consultas *Aggregate*, trazendo possíveis ganhos de desempenho, principalmente quando se tem muitas variáveis a serem pesquisadas.
* [Buscando informações de Interfaces de Comunicação](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/int_svr_status.ipynb) - Verificando informações de interfaces de comunicação (EPM Interfaces).
* [Exemplo de gáfico 3D e polar](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/matplotlib_3d_polar.ipynb) - Exemplo de como fazer um gráfico 3D e polar com dados de processo.
* [Lendo dados de arquivos TXT, CSV, XLSX e JSON](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/reading_from_file.ipynb) - Exemplos de leitura de dados de diversos tipos de arquivos (TXT, CSV, XLSX e JSON).
* [Lendo dados de processo e convertendo para DataFrame do Pandas](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/sample01.ipynb) - leitura de dados de processo do EPM Server (OPC UA Server), criação de um DataFrame do módulo Pandas e exemplos de análises.
* [Análise do conforto térmico](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/sample02.ipynb) - leitura de dados de processo do EPM Server (OPC UA Server), criação de um DataFrame do módulo Pandas e análise de conforto térmico ([Webinar - Análise de Dados com Python e Dashboard Web](https://youtu.be/IYg5yutkIhw)).
* [Gerando relatórios em HTML e/ou PDF](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/PdfReport_Temperatures.ipynb) - Gerando relatórios em HTML ou PDF, abordando questões sobre Jinja2, Base64, lendo informações de variáveis de ambiente, criando séries temporais na Pandas convertendo UTC para hora local.
* [CRUD em Basic Variables](https://github.com/elipsesoftware/epmwebapi/blob/master/exemplos/basicvariables_CRUD.ipynb) - Criando, alterando configurações e excluindo Basic Variables do EPM Server.




