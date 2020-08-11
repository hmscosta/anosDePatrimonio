

class Operacoes(object):

  def pesquisarNome(self,codigoCandidato, datasetCandidatos):
    nome = ""
    for row in datasetCandidatos:
      if (row[15] == codigoCandidato):
        nome = row[17]
        break
      else:
        continue
    #print (codigoCandidato +"-----" + nome)
    return nome

  #Metodo para testes de debug
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