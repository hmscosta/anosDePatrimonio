import csv
import sys

class Arquivos(object):

    def __init__(self):
        print("Objeto arquivo criado")

    def criarReaderCSV(self, arquivoParaLeitura):
        dados = csv.reader(arquivoParaLeitura, delimiter=';', quotechar='"')
        dados.next() 
        return dados

    def fecharArquivo(self,arquivoParaFechar):
        print("Fechando arquivo: " + arquivoParaFechar.name)
        arquivoParaFechar.close()

    def abrirArquivo(self, caminho):
        arquivoAberto = open(caminho)
        print("Abrindo arquivo: " + arquivoAberto.name)
        return arquivoAberto
   
    def printTeste(self):
        print("Testando classe")

