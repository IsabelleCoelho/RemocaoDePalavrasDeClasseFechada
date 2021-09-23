import sys
import os
from os import chdir, listdir
import spacy

pln = spacy.load('pt_core_news_md')
classesFechadas = ['ADP', 'AUX', 'CCONJ', 'SCONJ', 'PUNCT', 'PRON', 'DET', 'PART', 'SYM']

def palavraEClasseFechada(palavra):
    if palavra.pos_ in classesFechadas:
        return True
    return False

def removerPalavrasClasseFechada(texto):
    textoPreProcessado = pln(texto)
    textoProcessado = ""
    for palavra in textoPreProcessado:
        if palavraEClasseFechada(palavra) == False:
            textoProcessado += str(palavra) + " "
    return textoProcessado


if __name__ == "__main__":
    caminhoDiretorio = sys.argv[1]

    if(os.path.exists(caminhoDiretorio)):
        with open(caminhoDiretorio, 'r') as doc:
            texto = doc.read()
            palavrasClasseAberta = removerPalavrasClasseFechada(texto)
            print(palavrasClasseAberta)
    else:
        print("Caminho para diretório inválido. Por favor, tente novamente!")