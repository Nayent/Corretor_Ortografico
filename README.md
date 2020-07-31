<h1> Corretor Ortografico</h1>

### Tópicos 

* [Descrição e Funcionalidades do Projeto](#descrição-e-funcionalidades-do-projeto)

* [Dependências e Libs Instaladas](#dependências-e-libs-instaladas)

* [Data Base](#data-base)

## Descrição e Funcionalidades do Projeto

<p align = 'justify'> Código gerado em Python com o intuito de fazer correção ortografica, na lingua portuguesa(BR), em palavras que possuem erros de apenas uma casa de distancia, ou seja, erros de apenas uma letra, independente do que seja, letra faltando, letra a mais, letra sem acento e letras trocadas.</p>

<p align = 'justify'> Existem três tipos de saidas: </p>
<p> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp - Se for digitado uma palavra correta, sairá a palavra digita com a primeira letra maiuscula.</p>
<p> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp - Se for digitado uma palavra errada, com o erro a apenas uma casa de distancia, sairá a palavra corrigida no final.</p>
<p> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp - Se for digitado uma palavra com varios erros a saida será a palavra digitada com um aviso de que a palavra possivelmente está incorreta.</p>

<p align = 'justify'> Exemplos de correções:</p>

- Palavra digitada = docunento
  - Saida = Documento
  
- Palavra digitada = pyhton
  - Saida = Python
  
- Palavra digitada = armazzenamento
  - Saida = Armazenamento

## Dependências e Libs Instaladas

<p align = 'justify'> Foi utilizado apenas uma biblioteca para este projeto, sendo ela a nltk (Natural Language TooKit). Sendo ela utilizada para o processamento do banco de dados utilizado, enquanto que para a montagem do corretor ortografico foi utilizado apenas as bibliotecas padrões do Python.</p>

## Data Base

<p align = 'justify'> Para realizar o corretor foi utilizado um banco de dados com posts encontrados no site da Alura, pegando todas as palavras utilizadas nesses posts para utilizar como padrão para o corretor.</p>
