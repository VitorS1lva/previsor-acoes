from coletor_info import *
import matplotlib.pyplot as plt

def visualizaInfo():
    plt.figure(figsize=(6,6))
    plt.plot(cotacao_empresa['Close'])
    #plt.xticks(range(0,cotacao_empresa.shape[0],100), cotacao_empresa['Date'].loc[::100], rotation=35)
    plt.xlabel('Data', fontsize=15)
    plt.ylabel('Preço Fechamento', fontsize=18)
    plt.title('Histórico Fechamento PETR4.SA', fontsize=30)
    plt.show()

visualizaInfo()