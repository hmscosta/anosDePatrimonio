import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
from Arquivos import Arquivos
from Operacoes import Operacoes
reload(sys)
sys.setdefaultencoding("latin-1")


class Program:
      
  def main():
    objetoArquivos = Arquivos()
    objetoOperacoes = Operacoes()
    arquivoBens = objetoArquivos.abrirArquivo('dataset/bem_candidato_2018_AP.csv')
    arquivoCandidatos = objetoArquivos.abrirArquivo('dataset/consulta_cand_2018_AP.csv')
    datasetBens = objetoArquivos.criarReaderCSV(arquivoBens)
    datasetCandidatos = objetoArquivos.criarReaderCSV(arquivoCandidatos)
    for row in datasetBens:
      nome = objetoOperacoes.pesquisarNome(row[11], datasetCandidatos)
      arquivoCandidatos.seek(0)
      datasetCandidatos.next() 
      print ("Codigo candidato: " + row[11] + "\n" +
            "Nome: " + nome.decode('latin-1') + "\n" +
            "Lista de bens: " + row[14] + "\n" +
            "Valor (R$): " + row[16] + "\n" 
            )
    objetoArquivos.fecharArquivo(arquivoBens)
    objetoArquivos.fecharArquivo(arquivoCandidatos)


  if __name__ == "__main__":
    main()
  




#labels = ['1995', '1996', '1997', '1998', '1999']
#men_means = [20, 35, 30, 35, 27]
#women_means = [25, 32, 34, 20, 25]
#men_std = [2, 3, 4, 1, 2]
#women_std = [3, 5, 2, 3, 3]
#width = 0.35       # the width of the bars: can also be len(x) sequence
#fig, ax = plt.subplots()
#ax.bar(labels, men_means, width, yerr=men_std, label='Men')
#ax.set_ylabel('Valor (R$)')
#ax.set_title('Patrimonio ao longo dos anos')
#ax.legend()
#plt.show()