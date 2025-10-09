import epmwebapi as epm
import pytz
import datetime

# Método para não expor usuário e senha do EPM no código fonte
import getpass
user = input('EPM user:')
password = getpass.getpass("EPM password:")

# Criando a conexão com o EPM Web Server.
epmConn = epm.EpmConnection('https://localhost:44340', 'https://localhost:44339', user, password)

# Definindo fuso-horário a ser utilizado.
tz_sp = pytz.timezone('America/Sao_Paulo')

# Definindo intervalo de consulta com base no fuso-horário.
endTime = datetime.datetime.now(tz_sp)
iniTime = endTime - datetime.timedelta(hours=2)
processInterval = datetime.timedelta(minutes=10)

queryPeriod = epm.QueryPeriod(iniTime, endTime)

aggTimeAvgDetails = epm.AggregateDetails(processInterval, epm.AggregateType.TimeAverage)

path = 'MemoriaEpmServer'

bv = epmConn.getDataObjects(path)

# Efetuando a consulta. Como os dados no server estão em UTC,
# o resultado da consulta terá o timestamp em formato UTC também,
# mas com o período equivalente ao período informado de acordo com o fuso-horário informado.
result= bv[path].historyReadAggregate(aggTimeAvgDetails, queryPeriod)

epmConn.close()
print(result)
