import csv
import pyodbc
import numpy as np
import datetime

def readCSVfile(CSVFile):
    '''
        Este método carrega as informações de um arquivo CSV com as informações abaixo:
        - TagFrom: informa o tag original do histórico do E3
        - TagTo: Informa a variável que receberá os dados no EPM. Pode ser o nome de uma BasicVariable ou o endereço de uma medida do model (o endereço é separado por bara (/).
        - IsObj: True se o TagTo for uma medida (AliasProperty) do modelo e False se o TagTo for uma BasicVariable.
    '''
    csvfile = open(CSVFile, newline='')
    tagList = csv.reader(csvfile, delimiter=';', quotechar='|')
    tagDict = []
    for row in tagList:
        tagDict.append({'From': row[0], 'To': row[1], 'IsObj': row[2]})
    return tagDict

def readAccessHist(MDBFile, TableName, TagFrom):
    '''
        Configura a string de conexão para um arquivo do MS Access (MDB).
        Parâmetros:
        - MDBFile: Endereço do arquivo MDB que contém os dados históricos do E3.
        - TableName: Nome da tabela do histórico do E3.
        - TagFrom: PathName do tag a ser consultado.
    '''
    
    DRV = r'{Microsoft Access Driver (*.mdb, *.accdb)}'
    
    # Define the connection string
    conn_str = 'DRIVER={};DBQ={};'.format(DRV,MDBFile)
    
    return selectData('Access', conn_str, TableName, TagFrom)

def readSQLHist(SERVER, DATABASE, USERNAME, PASSWORD, TableName, TagFrom):
    '''
        Configura a string de conexão para uma base de dados SQL Server.
        Parâmetros:
        - SERVER: Nome/endereço do servidor do SQL Server.
        - DATABASE: Nome da base de dados onde estão os dados históricos.
        - USERNAME: Nome do usuário para conexão ao servidor SQL.
        - PASSWORD: Senha do usuário informado.
        - TableName: Nome da tabela do histórico do E3.
        - TagFrom: PathName do tag a ser consultado.
    '''
    
    DRV = r'{ODBC Driver 18 for SQL Server}'
    
    # Define the connection string
    conn_str = 'DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(DRV, SERVER, DATABASE, USERNAME, PASSWORD)
    
    return selectData('SQL', conn_str, TableName, TagFrom)

def selectData(dbType, connectionString, TableName, TagFrom):
    '''
        Método para buscar os dados históricos do E3 na base de dados informada.
        Parâmetros:
        - dbType: tipo do servidor de banco de dados (Access, SQL).
        - connectionString: string para conexão à base de dados.
        - TableName: Nome da tabela do histórico do E3.
        - TagFrom: PathName do tag a ser consultado.
    '''
    
    conn = pyodbc.connect(connectionString)
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT FieldName FROM {}_Fields Where FieldSource Like '{}'".format(TableName, TagFrom))
    fName = cursor.fetchall()[0][0]
    
    # epm ndarray data format.
    desc = np.dtype([('Value', '>f8'), ('Timestamp', 'object'), ('Quality', 'object')])

    i = 0
    totalData = []
    startDate = datetime.datetime(2000, 1, 1)
    
    dateTag = "#"
    if dbType == 'SQL':
        dateTag = "'"
        
    exQuery = True
    while exQuery:
        cursor.execute("SELECT TOP 1000 E3TimeStamp, {}_Quality, {} FROM {} WHERE E3TimeStamp > {}{}{}".format(fName, fName, TableName, dateTag, startDate, dateTag))
        content = cursor.fetchall()
        startDate = content[-1][0]
        if len(content) <= 1:
            exQuery = False
            continue
            
        for row in content:
            TS = row[0]
            if row[1] >= 192:
                Q = 0
            else:
                Q = 2147483648
            V = row[2]
            totalData.append({'Timestamp': TS, 'Quality': Q, 'Value': V})

    myData = np.empty(len(totalData), dtype=desc)
    
    while i < len(totalData):
        myData['Timestamp'][i] = totalData[i]['Timestamp']
        myData['Quality'][i] = totalData[i]['Quality']
        myData['Value'][i] = totalData[i]['Value']
        i += 1
    return myData

def WriteEPMHistory(EPMConn, TagName, IsObj, DataObj):
    '''
        Método para escrever os dados de um ndArray no formato do EPM em um objeto do EPM.
        Parâmetros:
        - EPMConn: Objeto de conexão com o EPM.
        - TagName: Nome do objeto do EPM que irá receber os dados. Pode ser uma BasicVariable ou uma medida do modelo.
        - IsObj: True se o TagName for uma medida (AliasProperty) do modelo e False se o TagName for uma BasicVariable.
        - DataObj: Objeto ndarray com os dados a serem escritos. O formato do ndarray deve ser, obrigatoriamente, conforme a descrição abaixo:
            dtype([('Value', '>f8'), ('Timestamp', 'object'), ('Quality', 'object')])
    '''

    if IsObj:
        bv = EPMConn.getObjects(TagName)
    else:
        bv = EPMConn.getDataObjects(TagName)
    bv[TagName].historyUpdate(DataObj)