import nltk
# nltk.download('punkt')

def separa_palavras(lista):

  lista_separada = []

  for palavra in lista:
    if palavra.isalpha():
      lista_separada.append(palavra)

  return lista_separada


def normalizacao(lista):
  lista_normalizada = []

  for palavra in lista:
    lista_normalizada.append(palavra.lower())

  return lista_normalizada



def construir_palavra(palavra):
  fatias = []

  for i in range(len(palavra) + 1):
    fatias.append((palavra[:i], palavra[i:]))

  palavras = inserir_letras(fatias)
  palavras += deletando_caracter(fatias)
  palavras += troca_letra(fatias)
  palavras += inverte_letra(fatias)

  return palavras


def inserir_letras(fatias):
  novas_palavras = []

  letras = 'abcdefghijklmnopqrstuvwxyzáâàãéêèẽíîìĩóôõòúûùũç'
  for E, D in fatias:
    for letra in letras:
      novas_palavras.append(E + letra + D)

  return novas_palavras


def probabilidade(palavra):
  return frequencia[palavra] / len(artigos)


def corretor(palavra):
  teste2 = 0

  if palavra in artigos:
    return print(palavra.title())
  else:
    candidatos = [palavra]

    palavras_geradas = construir_palavra(palavra)

    for i in palavras_geradas:
      if i in artigos:
        candidatos.append(i)
        teste2 += 1

    palavra_correta = max(candidatos, key=probabilidade)
    if palavra_correta in artigos:
      return print(palavra_correta.title())
    else:
      return print(palavra.title() + ' (Palavra Possivelmente incorreta)')

def deletando_caracter(fatias):
  novas_palavras = []
  for E, D in fatias:
    novas_palavras.append(E + D[1:])
  return novas_palavras


def troca_letra(fatias):
  novas_palavras = []

  letras = 'abcdefghijklmnopqrstuvwxyzáâàãéêèẽíîìĩóôõòúûùũç'

  for E, D in fatias:
    for i in letras:
      novas_palavras.append(E + i + D[1:])

  return novas_palavras


def inverte_letra(fatias):
  novas_palavras = []

  for E, D in fatias:
    if len(D) > 1:
      novas_palavras.append(E + D[1] + D[0] + D[2:])

  return novas_palavras


def gerador_duplo(palavra):
  gerador = construir_palavra(construir_palavra(palavra))
  return gerador


f = open("Data/Corretor/Artigos.txt", "r", encoding='utf-8')
artigos = f.read()
f.close()

artigos = nltk.tokenize.word_tokenize(artigos)

artigos = separa_palavras(artigos)

artigos = normalizacao(artigos)

artigos_sep = set(artigos)

frequencia = nltk.FreqDist(artigos)

palavra_user = ' '

while palavra_user != 1:
  palavra_user = input("Digite uma palavra >> ")
  corretor(palavra_user)
