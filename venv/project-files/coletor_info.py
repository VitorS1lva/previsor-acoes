from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

hoje = date.today()
h1 = hoje.strftime("%m/%d/%y")
ontem = "01/01/2013"
cotacao_empresa=web.DataReader('PETR4.SA', data_source='yahoo', start=ontem, end=hoje)

def pegaCotacao():
    codigo_empresa=input(str("[*] Insira o código da empresa: "))
    data_inicial=input(str("[*] Insira a data inicial (MM/DD/YYYY): "))
    data_final=input(str("[*] Insira a data final (MM/DD/YYYY): "))
    print(cotacao_empresa)
    cotacao_empresa["Adj Close"].plot(figsize=(8,8))
    plt.show()

#def leInfo():
    #tabela_empresas=pd.read_excel('previsor-acoes\ibov.xlsx')
    #for empresa in tabela_empresas['CODIGO']:
        #print(empresa)
        #cotacao = web.DataReader(f'{empresa}.SA', data_source='yahoo', start='04/01/2022', end='04/30/2022')
        #print(cotacao)
        #cotacao['Close'].plot(figsize=(8,8))
        #plt.show()

#leInfo()