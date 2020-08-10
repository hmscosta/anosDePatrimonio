import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
reload(sys)
sys.setdefaultencoding("latin-1")
#Funcao para testes de debug
def testes():
  minhaString = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
  print('----------------------------')
  print(minhaString)
  print(minhaString[0])
  print(minhaString[1])
  print(minhaString[2])
  print(minhaString[3])
  print(minhaString[4])
  print("----------------------------")
  for row in minhaString:
    if(row == "Terceiro"):
      print(row)
      break
    else:
      continue
  print("ROW: "+ row)


def pesquisarNome(codigoCandidato, datasetCandidatos):
  nome = ""
  for row in datasetCandidatos:
    if (row[15] == codigoCandidato):
      nome = row[17]
      break
    else:
      continue
  #print (codigoCandidato +"-----" + nome)
  return nome
  


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


arquivoBens = open('dataset/bem_candidato_2018_AP.csv')
arquivoCandidatos = open('dataset/consulta_cand_2018_AP.csv')
datasetBens = csv.reader(arquivoBens, delimiter=';', quotechar='"')
datasetCandidatos = csv.reader(arquivoCandidatos, delimiter=';', quotechar='"')
datasetBens.next() 
datasetCandidatos.next() 
#testes()
for row in datasetBens:
  nome = pesquisarNome(row[11], datasetCandidatos)

  arquivoCandidatos.seek(0)
  datasetCandidatos.next() 
  print ("Codigo candidato: " + row[11] + "\n" +
         "Nome: " + nome.decode('latin-1') + "\n" +
         "Lista de bens: " + row[14] + "\n" +
         "Valor (R$): " + row[16] + "\n" 
        )

arquivoBens.close()
arquivoCandidatos.close()


