'''As respostas estão dentro de 3 aspas '''


# Exercícios de revisão:
#  Strings:
# 1. **Concatenação de Strings:**
#    Solicite ao usuário que insira seu primeiro nome e sobrenome separadamente e depois concatene-os para formar o nome completo.

'''# Solicita ao usuário que insira seu primeiro nome
primeiro_nome = input("Insira seu primeiro nome: ")

# Solicita ao usuário que insira seu sobrenome
sobrenome = input("Insira seu sobrenome: ")

# Concatena o primeiro nome e sobrenome para formar o nome completo
nome_completo = primeiro_nome + " " + sobrenome

# Imprime o nome completo
print("Seu nome completo é:", nome_completo)'''

#--------------------------------------------------------------------

# 2. **Contagem de Caracteres:**
#    Peça ao usuário que insira uma palavra e conte quantos caracteres a palavra possui.

'''# Solicita ao usuário que insira uma palavra
palavra = input("Insira uma palavra: ")

# Conta quantos caracteres a palavra possui
num_caracteres = len(palavra)

# Imprime o número de caracteres da palavra
print("A palavra inserida possui", num_caracteres, "caracteres.")'''

#--------------------------------------------------------------------


# 3. **Maiúsculas e Minúsculas:**
#    Peça ao usuário para inserir uma frase e converta-a completamente para letras minúsculas.

'''# Solicita ao usuário que insira uma frase
frase = input("Insira uma frase: ")

# Converte a frase para letras minúsculas
frase_minuscula = frase.lower()

# Imprime a frase convertida para letras minúsculas
print("Frase em letras minúsculas:", frase_minuscula)
'''

#--------------------------------------------------------------------
   
# 4. **Substituição de Caracteres:**
#    Solicite ao usuário que insira uma frase e substitua todas as ocorrências de uma determinada letra por outra letra especificada.

'''# Solicita ao usuário que insira uma frase
frase = input("Insira uma frase: ")

# Solicita ao usuário que insira a letra a ser substituída
letra_original = input("Insira a letra a ser substituída: ")

# Solicita ao usuário que insira a letra de substituição
letra_substituta = input("Insira a letra de substituição: ")

# Substitui todas as ocorrências da letra original pela letra substituta na frase
frase_substituida = frase.replace(letra_original, letra_substituta)

# Imprime a frase com as substituições realizadas
print("Frase com as substituições realizadas:", frase_substituida)
'''

#--------------------------------------------------------------------
   
# 5. **Divisão de Palavras:**
#    Peça ao usuário que insira uma frase e divida-a em uma lista de palavras.

'''# Solicita ao usuário que insira uma frase
frase = input("Insira uma frase: ")

# Divide a frase em uma lista de palavras
lista_palavras = frase.split()

# Imprime a lista de palavras
print("Lista de palavras:", lista_palavras)
'''

#--------------------------------------------------------------------

#--------------------------------------------------------------------

# Variáveis:
# 1. **Atribuição Simples:**
#    Atribua um número inteiro a uma variável e imprima seu valor.

'''# Atribui um número inteiro a uma variável
numero_inteiro = 10

# Imprime o valor da variável
print("O valor da variável é:", numero_inteiro)
'''

#--------------------------------------------------------------------
   
# 2. **Atribuição Múltipla:**
#    Atribua valores a múltiplas variáveis em uma única linha e depois imprima-as.

'''# Atribui valores a múltiplas variáveis em uma única linha
a, b, c = 1, 2, 3

# Imprime os valores das variáveis
print("Valor de a:", a)
print("Valor de b:", b)
print("Valor de c:", c)
'''

#--------------------------------------------------------------------
   
# 3. **Retribuição de Variáveis:**
#    Atribua um valor a uma variável, depois mude esse valor e imprima a variável novamente.

'''# Atribui um valor inicial à variável
numero = 10

# Imprime o valor inicial da variável
print("Valor inicial da variável:", numero)

# Modifica o valor da variável
numero = 20

# Imprime o novo valor da variável
print("Novo valor da variável:", numero)
'''

#--------------------------------------------------------------------
   
# 4. **Variáveis de Texto:**
#    Atribua uma string a uma variável e imprima-a.

'''# Atribui uma string a uma variável
minha_string = "Olá, mundo!"

# Imprime a variável
print(minha_string)'''


#--------------------------------------------------------------------
   
# 5. **Variáveis Numéricas:**
#    Atribua valores numéricos (inteiros ou de ponto flutuante) a variáveis e realize operações aritméticas simples com elas.

'''# Atribui valores numéricos a variáveis
numero_inteiro = 10
numero_flutuante = 3.5

# Realiza operações aritméticas com as variáveis
soma = numero_inteiro + numero_flutuante
subtracao = numero_inteiro - numero_flutuante
multiplicacao = numero_inteiro * numero_flutuante
divisao = numero_inteiro / numero_flutuante

# Imprime os resultados das operações
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
'''

#--------------------------------------------------------------------

#--------------------------------------------------------------------

# Manipulação de String:
# 1. **Capitalização:**
#    Converta uma string para todos os caracteres em maiúsculas.

'''# Define uma string
minha_string = "Olá, Mundo!"

# Converte a string para maiúsculas
string_maiuscula = minha_string.upper()

# Imprime a string em maiúsculas
print("String em maiúsculas:", string_maiuscula)
'''

#--------------------------------------------------------------------
   
# 2. **Substituição:**
#    Substitua todas as ocorrências de uma palavra em uma frase por outra palavra.

'''# Define a frase e as palavras a serem substituídas
frase = "O cachorro correu no parque. O cachorro é feliz."
palavra_original = "cachorro"
palavra_substituta = "gato"

# Substitui todas as ocorrências da palavra original pela palavra substituta na frase
frase_substituida = frase.replace(palavra_original, palavra_substituta)

# Imprime a frase com as substituições realizadas
print("Frase com as substituições realizadas:", frase_substituida)
'''

#--------------------------------------------------------------------
   
# 3. **Contagem de Substrings:**
#    Conte quantas vezes uma determinada substring ocorre em uma string.

'''# Define a string e a substring a ser contada
minha_string = "Olá, olá, mundo!"
substring = "olá"

# Conta quantas vezes a substring ocorre na string (ignorando maiúsculas e minúsculas)
ocorrencias = minha_string.lower().count(substring.lower())

# Imprime o número de ocorrências da substring na string
print("Número de ocorrências da substring na string:", ocorrencias)
'''

#--------------------------------------------------------------------
   
# 4. **Separação de String:**
#    Separe uma string em substrings com base em um caractere de delimitação.

'''# Define a string e o caractere de delimitação
minha_string = "maçã,uva,banana,morango"
caractere_delimitacao = ","

# Separa a string em substrings usando o caractere de delimitação
substrings = minha_string.split(caractere_delimitacao)

# Imprime as substrings resultantes
print("Substrings separadas:", substrings)
'''

#--------------------------------------------------------------------
   
# 5. **Remoção de Espaços:**
#    Remova todos os espaços em branco de uma string.

'''# Define a string com espaços em branco
minha_string = "Olá,    mundo!"

# Remove todos os espaços em branco da string
string_sem_espacos = minha_string.replace(" ", "")

# Imprime a string sem espaços em branco
print("String sem espaços em branco:", string_sem_espacos)
'''

#--------------------------------------------------------------------

#--------------------------------------------------------------------

# Fatiamento de String:
# 1. **Fatiamento Simples:**
#    Dada uma string, imprima apenas os primeiros três caracteres.

'''# Define a string
minha_string = "Python"

# Imprime os primeiros três caracteres da string
print("Primeiros três caracteres:", minha_string[:3])
'''

#--------------------------------------------------------------------
   
# 2. **Fatiamento com Intervalo:**
#    Imprima uma substring de uma string dada usando um intervalo.

'''# Define a string
minha_string = "Python é uma linguagem de programação poderosa"

# Define o intervalo de índices para a substring
inicio = 7
fim = 18

# Imprime a substring usando o intervalo de índices
print("Substring:", minha_string[inicio:fim])
'''

#--------------------------------------------------------------------
   
# 3. **Fatiamento Reverso:**
#    Imprima uma substring de uma string de trás para frente.

'''# Define a string
minha_string = "Python é uma linguagem de programação poderosa"

# Define o intervalo de índices para a substring de trás para frente
inicio = -13
fim = -1

# Imprime a substring de trás para frente
print("Substring de trás para frente:", minha_string[inicio:fim])
'''

#--------------------------------------------------------------------
   
# 4. **Fatiamento Alternado:**
#    Imprima uma substring de uma string pulando caracteres em intervalos específicos.

'''# Define a string
minha_string = "Python é uma linguagem de programação poderosa"

# Define o intervalo de índices para a substring pulando caracteres em intervalos específicos
inicio = 0
fim = len(minha_string)
passo = 2

# Imprime a substring pulando caracteres em intervalos específicos
print("Substring pulando caracteres em intervalos específicos:", minha_string[inicio:fim:passo])
'''

#--------------------------------------------------------------------
   
# 5. **Fatiamento com Índices Negativos:**
#    Imprima uma substring de uma string usando índices negativos.

'''# Define a string
minha_string = "Python é uma linguagem de programação poderosa"

# Define os índices negativos para a substring
inicio = -25
fim = -18

# Imprime a substring usando índices negativos
print("Substring com índices negativos:", minha_string[inicio:fim])
'''

#--------------------------------------------------------------------

#--------------------------------------------------------------------

# Números (Operações aritméticas, comparação, lógico):
# 1. **Operações Aritméticas Simples:**
#    Realize operações de adição, subtração, multiplicação e divisão entre dois números.

'''# Define os dois números
numero1 = 10
numero2 = 5

# Realiza as operações matemáticas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# Imprime os resultados das operações
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
'''

#--------------------------------------------------------------------
   
# 2. **Comparação de Números:**
#    Compare dois números e imprima se são iguais, diferentes, maiores ou menores.

'''# Define os dois números
numero1 = 10
numero2 = 5

# Compara os números e imprime o resultado
if numero1 == numero2:
    print("Os números são iguais.")
elif numero1 != numero2:
    print("Os números são diferentes.")
elif numero1 > numero2:
    print("O primeiro número é maior que o segundo.")
elif numero1 < numero2:
    print("O primeiro número é menor que o segundo.")
'''

#--------------------------------------------------------------------
   
# 3. **Operações Lógicas:**
#    Realize operações lógicas (E, OU, NÃO) entre duas variáveis booleanas.

'''# Define duas variáveis booleanas
booleano1 = True
booleano2 = False

# Realiza operações lógicas entre as variáveis booleanas
resultado_and = booleano1 and booleano2  # Operação AND
resultado_or = booleano1 or booleano2    # Operação OR
resultado_not = not booleano1           # Operação NOT

# Imprime os resultados das operações
print("Resultado da operação AND:", resultado_and)
print("Resultado da operação OR:", resultado_or)
print("Resultado da operação NOT:", resultado_not)
'''

#--------------------------------------------------------------------
   
# 4. **Arredondamento de Números:**
#    Arredonde um número de ponto flutuante para um número inteiro.

'''# Define um número de ponto flutuante
numero_flutuante = 3.7

# Arredonda o número para um número inteiro
numero_inteiro = round(numero_flutuante)

# Imprime o número inteiro arredondado
print("Número inteiro arredondado:", numero_inteiro)'''


#--------------------------------------------------------------------

#--------------------------------------------------------------------
   
# 5. **Conversão de Tipos:**
#    Converta um número inteiro para ponto flutuante e vice-versa, depois imprima-os.

'''# Convertendo um número inteiro para ponto flutuante
numero_inteiro = 5
numero_flutuante = float(numero_inteiro)
print("Número inteiro convertido para ponto flutuante:", numero_flutuante)

# Convertendo um número ponto flutuante para inteiro
numero_flutuante = 3.7
numero_inteiro = int(numero_flutuante)
print("Número ponto flutuante convertido para inteiro:", numero_inteiro)
'''

#--------------------------------------------------------------------

#--------------------------------------------------------------------

# Listas:
# 1. **Criação de Lista:**
#    Crie uma lista com alguns números inteiros e imprima-a.

'''# Cria uma lista com alguns números inteiros
numeros_inteiros = [1, 2, 3, 4, 5]

# Imprime a lista de números inteiros
print("Lista de números inteiros:", numeros_inteiros)
'''

#--------------------------------------------------------------------
   
# 2. **Acesso a Elementos:**
#    Acesse e imprima o terceiro elemento de uma lista.

'''# Define a lista
lista = [10, 20, 30, 40, 50]

# Acessa e imprime o terceiro elemento da lista
terceiro_elemento = lista[2]
print("Terceiro elemento da lista:", terceiro_elemento)
'''

#--------------------------------------------------------------------
   
# 3. **Adição de Elementos:**
#    Adicione um novo elemento ao final de uma lista e imprima a lista atualizada.

'''# Define a lista
lista = [10, 20, 30, 40, 50]

# Adiciona um novo elemento ao final da lista
novo_elemento = 60
lista.append(novo_elemento)

# Imprime a lista atualizada
print("Lista atualizada:", lista)
'''

#--------------------------------------------------------------------
   
# 4. **Remoção de Elementos:**
#    Remova o segundo elemento de uma lista e imprima a lista resultante.

'''# Define a lista
lista = [10, 20, 30, 40, 50]

# Remove o segundo elemento da lista
lista.pop(1)

# Imprime a lista resultante
print("Lista resultante:", lista)
'''

#--------------------------------------------------------------------
   
# 5. **Tamanho da Lista:**
#    Imprima o número de elementos presentes em uma lista.

'''# Define a lista
lista = [10, 20, 30, 40, 50]

# Imprime o número de elementos na lista
print("Número de elementos na lista:", len(lista))
'''

#--------------------------------------------------------------------

#--------------------------------------------------------------------

# Operações com Listas:
# 1. **Concatenação de Listas:**
#    Concatene duas listas e imprima a lista resultante.

'''# Define as duas listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatena as duas listas
lista_concatenada = lista1 + lista2

# Imprime a lista resultante
print("Lista resultante da concatenação:", lista_concatenada)'''

#--------------------------------------------------------------------
   
# 2. **Ordenação de Lista:**
#    Ordene os elementos de uma lista em ordem crescente e imprima-a.

'''# Define a lista
lista = [10, 5, 8, 3, 9]

# Ordena os elementos da lista em ordem crescente
lista.sort()

# Imprime a lista ordenada
print("Lista ordenada em ordem crescente:", lista)
'''
   

#--------------------------------------------------------------------
# 3. **Reversão de Lista:**
#    Inverta os elementos de uma lista e imprima-a.

'''# Define a lista
lista = [10, 20, 30, 40, 50]

# Inverte os elementos da lista
lista.reverse()

# Imprime a lista invertida
print("Lista invertida:", lista)
'''

'''# Define a lista
lista = [10, 20, 30, 40, 50]

# Inverte os elementos da lista usando indexação reversa
lista_invertida = lista[::-1]

# Imprime a lista invertida
print("Lista invertida:", lista_invertida)
'''

#--------------------------------------------------------------------
   
# 4. **Contagem de Elementos:**
#    Conte quantas vezes um determinado elemento ocorre em uma lista.

'''# Define a lista
lista = [1, 2, 3, 4, 1, 2, 1, 3, 1]

# Conta quantas vezes o elemento 1 ocorre na lista
ocorrencias = lista.count(1)

# Imprime o número de vezes que o elemento ocorre na lista
print("O elemento 1 ocorre", ocorrencias, "vezes na lista.")
'''
#--------------------------------------------------------------------
   
# 5. **Cópia de Lista:**
#    Copie uma lista para outra variável e imprima ambas para verificar se são iguais.

'''# Define a lista
lista_original = [1, 2, 3, 4, 5]

# Copia a lista para outra variável usando a função list()
lista_copiada = list(lista_original)

# Imprime ambas as listas para verificar se são iguais
print("Lista original:", lista_original)
print("Lista copiada:", lista_copiada)
'''

'''# Define a lista
lista_original = [1, 2, 3, 4, 5]

# Copia a lista para outra variável usando o operador de fatiamento
lista_copiada = lista_original[:]

# Imprime ambas as listas para verificar se são iguais
print("Lista original:", lista_original)
print("Lista copiada:", lista_copiada)
'''

#--------------------------------------------------------------------

#--------------------------------------------------------------------

# Fatiamento de Lista:
# 1. **Fatiamento Simples:**
#    Dada uma lista, imprima apenas os primeiros três elementos.

'''# Define a lista
lista = [10, 20, 30, 40, 50]

# Imprime os primeiros três elementos da lista
primeiros_tres_elementos = lista[:3]
print("Os primeiros três elementos da lista:", primeiros_tres_elementos)
'''
#--------------------------------------------------------------------
   
# 2. **Fatiamento com Intervalo:**
#    Imprima uma sublista de uma lista dada usando um intervalo.

'''# Define a lista
lista = [10, 20, 30, 40, 50]

# Define o intervalo para a sublista (do segundo ao quarto elemento)
inicio_intervalo = 1  # Segundo elemento (índice 1)
fim_intervalo = 4     # Quarto elemento (índice 4 não incluso)

# Imprime a sublista usando o intervalo especificado
sublista = lista[inicio_intervalo:fim_intervalo]
print("Sublista da lista original:", sublista)
'''

#--------------------------------------------------------------------
   
# 3. **Fatiamento Reverso:**
#    Imprima uma sublista de uma lista de trás para frente.

'''# Define a lista
lista = [10, 20, 30, 40, 50]

# Define o intervalo para a sublista (do quarto ao segundo elemento, de trás para frente)
inicio_intervalo = 3  # Quarto elemento (índice 3)
fim_intervalo = 0     # Segundo elemento (índice 0 não incluso)
passo = -1            # Passo negativo para percorrer a lista de trás para frente

# Imprime a sublista de trás para frente usando o intervalo especificado
sublista = lista[inicio_intervalo:fim_intervalo:passo]
print("Sublista da lista original de trás para frente:", sublista)
'''

#--------------------------------------------------------------------
   
# 4. **Fatiamento Alternado:**
#    Imprima uma sublista de uma lista pulando elementos em intervalos específicos.

'''# Define a lista
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Define o intervalo para a sublista (pulando de dois em dois elementos)
inicio_intervalo = 0  # Primeiro elemento (índice 0)
fim_intervalo = len(lista)  # Último elemento (tamanho da lista)
passo = 2  # Intervalo específico (pulando de dois em dois elementos)

# Imprime a sublista usando o intervalo especificado
sublista = lista[inicio_intervalo:fim_intervalo:passo]
print("Sublista da lista original pulando elementos em intervalos específicos:", sublista)
'''

#--------------------------------------------------------------------
   
# 5. **Fatiamento com Índices Negativos:**
#    Imprima uma sublista de uma lista usando índices negativos.

'''# Define a lista
lista = [10, 20, 30, 40, 50, 60, 70, 80]

# Define os índices negativos para a sublista
inicio_intervalo = -4  # Índice negativo para o quarto elemento a partir do final
fim_intervalo = -1    # Índice negativo para o primeiro elemento a partir do final

# Imprime a sublista usando os índices negativos especificados
sublista = lista[inicio_intervalo:fim_intervalo]
print("Sublista da lista original usando índices negativos:", sublista)
'''

#--------------------------------------------------------------------

#--------------------------------------------------------------------

# Tuplas:
# 1. **Criação de Tupla:**
#    Crie uma tupla com alguns valores e imprima-a.

'''# Criar uma tupla com alguns valores
minha_tupla = (10, 20, 30, 40, 50)

# Imprimir a tupla
print("Minha tupla:", minha_tupla)
'''

#--------------------------------------------------------------------
   
# 2. **Acesso a Elementos:**
#    Acesse e imprima o terceiro elemento de uma tupla.

'''# Definir a tupla
minha_tupla = (10, 20, 30, 40, 50)

# Acessar e imprimir o terceiro elemento da tupla
terceiro_elemento = minha_tupla[2]
print("Terceiro elemento da tupla:", terceiro_elemento)
'''

#--------------------------------------------------------------------
   
# 3. **Concatenação de Tuplas:**
#    Concatene duas tuplas e imprima a tupla resultante.

'''# Definir as duas tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenar as duas tuplas
tupla_concatenada = tupla1 + tupla2

# Imprimir a tupla resultante
print("Tupla resultante da concatenação:", tupla_concatenada)
'''
#--------------------------------------------------------------------
   
# 4. **Comprimento da Tupla:**
#    Imprima o número de elementos presentes em uma tupla.

'''# Definir a tupla
minha_tupla = (10, 20, 30, 40, 50)

# Imprimir o número de elementos presentes na tupla
num_elementos = len(minha_tupla)
print("Número de elementos na tupla:", num_elementos)
'''

#--------------------------------------------------------------------
   
# 5. **Imutabilidade da Tupla:**
#    Tente alterar um elemento de uma tupla e observe o erro gerado.

'''# Definir a tupla
minha_tupla = (1, 2, 3)

# Tentar alterar o segundo elemento da tupla
minha_tupla[1] = 5  # Isso resultará em um erro TypeError
'''

#--------------------------------------------------------------------

#--------------------------------------------------------------------

# Dicionários:
# 1. **Criação de Dicionário:**
#    Crie um dicionário com alguns pares chave-valor e imprima-o.

'''# Criar um dicionário com alguns pares chave-valor
meu_dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Imprimir o dicionário
print("Meu dicionário:", meu_dicionario)
'''

#--------------------------------------------------------------------
   
# 2. **Acesso a Valores:**
#    Acesse e imprima o valor associado a uma chave específica em um dicionário.

'''# Definir o dicionário
meu_dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Acessar e imprimir o valor associado à chave "idade"
valor_idade = meu_dicionario["idade"]
print("Valor associado à chave 'idade':", valor_idade)
'''

#--------------------------------------------------------------------
   
# 3. **Adição de Novos Pares:**
#    Adicione um novo par chave-valor a um dicionário

'''# Definir o dicionário inicial
meu_dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Adicionar um novo par chave-valor ao dicionário
meu_dicionario["email"] = "joao@example.com"

# Imprimir o dicionário atualizado
print("Dicionário após adicionar um novo par chave-valor:", meu_dicionario)
'''

#--------------------------------------------------------------------
