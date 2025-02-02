#explorando o ambiente R

# 1.comando help(nome_da_funcao) para obter ajuda sobre uma função específica.
help("sin")

#2.comando ?nome_da_funcao para obter uma visão rápida da função.
?sqrt

#3.objeto do tipo numeric com o comando c(1, 2, 3, 4, 5). Nome Teste1
nome.teste1 <- c(1, 2, 3, 4, 5)

#4.4.objeto do tipo character com o comando c("a", "b", "c", "d", "e"). Nome Teste2
nome.teste2 <- c("a", "b", "c", "d", "e")


minha = 45
var=20
minha-var->minha_var

#comando ls() para verificar os objetos disponíveis no ambiente. Use rm() para remover um objeto da memória.

is.numeric(nome.teste1)
is.numeric(nome.teste2)
is.numeric(minha_var)

is.character(nome.teste1)
is.character(nome.teste2)
is.character(minha_var)

rm(nome.teste1)
rm(nome.teste2)
rm(minha_var)

is.numeric(nome.teste1)


lugar=""

#operações básicas

#1 função paste para concatenar textos. 

lugar= "UFMG!"
paste("Que", "disciplina", "dífícil", lugar , sep = " " )

#2 prática

cidade<- "Belo Horizonte"
estado<- "MG"

paste(cidade, "-", estado)

#3. vetores numéricos x e y, com 5 elementos cada. Utilize os operadores aritméticos (+, -, *, /) para realizar cálculos.

x<- c(1:5)
y<- c(20:25)

x+y
y-x
y*x
x/y

#4. Crie dois vetores lógicos a e b, com 3 elementos cada. Utilize os operadores lógicos (&,|, !) para realizar comparações lógicas.

a<- c(7:9)
b<- c(0:2)

a&b 
a|b
a!=b

#5. Utilize o comando ifelse() para realizar decisões condicionais, use os vetores dos dois exercícios anteriores.

ifelse(a<=8, "Aprova", "Reprova");ifelse(b>=1, "Aprova", "reprova")

#Vetores e Matrizes:

#1.Crie vetores com diferentes tipos de dados (números, texto, lógicos).

num<- c(15, 01, 20, 05)
tex<- c("a", "n" ,"i", "v", "e", "r", "s", "a", "r", "i", "o")
log<- c("FALSE", "FALSE", "TRUE", "TRUE")

#Combine vetores com o comando c(). O que acontece com os tipos de dados nas diferentes combinações? Pode usar a função class().
comb<- c(15, "n", "TRUE", 05)
comb2<- c(tex, log)
comb3<- c(num,log)

class(comb)
class(num)
class(tex)
class(comb2)
class(comb3)


#Acesse elementos de um vetor com o operador [].

ac<- num[2]
ac2<- tex[3:6]
ac3<- log[c(1, 4)]

print(c(ac, ac2, ac3))

#4.Dado o vetor booleano a seguir de resultados diários da B3. Quantos dias a bolsa subiu? Qual a proporção de dias em se produziu uma subida na bolsa? Use sum() e mean().

bolsa_subiu<- c(TRUE,TRUE,FALSE,FALSE,TRUE,FALSE,TRUE,FALSE)
dia_bolsa_subiu<- sum(bolsa_subiu)
prop_bolsa_subiu<- mean(bolsa_subiu)
print(dia_bolsa_subiu)
print(prop_bolsa_subiu)

#5.O código abaixo vai guardar três números inteiros entre 0 e 10. Determine se: são números maiores do que 5? são menores do que 4? São números pares?

segredo<- round(runif(3, min=0, max=10))

ifelse(segredo<4, TRUE, FALSE)
ifelse(segredo>5, TRUE, FALSE)
any(segredo %% 2==0)

#6.Crie o código para descobrir os números guardados no vetor segredo.

print(segredo)

#Crie matrizes com o comando matrix().

matrix1<- matrix(data = c(1:25), nrow = 5 , ncol = 5)
print(matrix1)

#Acesse elementos de uma matriz com os operadores

print(matrix1[2, 5])
coluna<- matrix1[, 4]
print(coluna)
coluna2<- matrix1[, c(5, 3)]
print(coluna2)
linha1<- matrix1[2, ]
print(linha1)
linha2<- matrix1[, c(3, 4)]

#Vetores e Operações Básicas:

#1.O seguinte código cria dois vetores de 55 e 40 elementos

vetor1 <- runif(55, 12, 40)
vetor2 <- rnorm(40, 25, 8)

vetor1[2]<- NA

#2.Utilize a função mean() para calcular a média dos vetores.

#média
media_1<- mean(vetor1, na.rm = TRUE)
media_2<- mean(vetor2)

média<- c(media_1, media_2)
print(média)

#mediana
mediana_1<- median(vetor1, na.rm = TRUE)
mediana_2<- median(vetor2)

mediana<- c(mediana_1, mediana_2)
print(mediana)

#desvio padrão
dp1<- sd(vetor1, na.rm = TRUE)
dp2<- sd(vetor2)

desvio.padrão<- c(dp1, dp2)
print(desvio.padrão)

#resumo estático dos vetores

summary(média, mediana, desvio.padrão)


#7.Crie um vetor vazio e adicione 7 valores numéricos entre 10 e 50 a ele.

vetor_teste<- numeric(0)
for (i in 1:7) {
  valor<- sample(10:50, 7)
  
}
print(valor)

#8.Encontre a soma, a média e o produto do vetor anterior.

sum(valor)
mean(valor)
prod(valor)

#10.Conte o número de valores dentro de um intervalo específico em um vetor, por exemplo entre 15 e 40.

valor1<- sample(10:50)
inicio <- 15
fim<- 40

num_valores_intervalo<- sum(valor1 >= inicio & valor1 <= fim)

print(num_valores_intervalo)

sum(2, 7)


#1.Crie uma lista com cinco posições onde em cada uma contém valores aleatórios com diferente número de elementos.

(lista_familia<- list(nome= "Deise", idade= 14, cidade= "Rio de janeiro", simbolo= "@", quer= "médicina" ))

#3 2.Conte o número de elementos da lista anterior. Quantos elementos tem a posição (chave) 2?
Num_da_posição<- length(lista_familia[3])
print(Num_da_posição)

#3.Adicione um par de elementos com nomes ou chaves a uma lista existente.
(lista_familia<- c(lista_familia, cabelo= "castanho"))

#Trabalhando com Strings:
#1.Converter uma string de caracteres em um nome de variável, use a função assign(). Atribua o vetor c(24,35,65) e essa variável e mostre a média da mesma.

assign("Kaua", c(24, 35, 65))
print(Kaua)
median(Kaua)

#2.Conte o número de caracteres em uma string (nchar()).

(nchar("Kaua"))

#3 
kaua <- c(21, "carioca")
class(kaua)

# 4

kaua <- c(21, "carioca", 35, "rio", 42)

kaua_numeric <- as.numeric(kaua)

posicoes_numeros <- !is.na(kaua_numeric)

numeros_filtrados <- kaua_numeric[posicoes_numeros]


print("Vetor original:")
print(kaua)
print("")

print("Vetor convertido para numérico:")
print(kaua_numeric)
print("")

print("Posições onde existem números:")
print(posicoes_numeros)
print("")

print("Números filtrados:")
print(numeros_filtrados)


#5

paste("eu", "gosto", "de", "frutas")

#dataframes
#1

textos <- c("texto1", "texto2", "texto3", "texto4", "texto5", "texto6", "texto7", "texto8", "texto9", "texto10")
numeros <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
logicos <- c(TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE)
fatores <- factor(c("A", "B", "C", "A", "B", "C", "A", "B", "C", "A"))

data_frame <- data.frame(Texto = textos, Numero = numeros, Logico = logicos, Fator = fatores)

print(data_frame)

#2

data_frame[1, 2] <- 20
data_frame[2, 3] <- FALSE
print(data_frame)

#3

filtro_numeros <- subset(data_frame, Numero > 5)

filtro_logicos <- subset(data_frame, Logico == TRUE)

filtro_fatores <- subset(data_frame, Fator == "B")

print(filtro_numeros)

print(filtro_logicos)

print(filtro_fatores)



#4

summary(data_frame)

#5

medias_por_nivel <- aggregate(data_frame$Numero, by = list(data_frame$Fator), FUN = mean)

colnames(medias_por_nivel) <- c("Fator", "Media_Numero")

print(medias_por_nivel)

#6

soma_verdadeiros <- sum(data_frame$Numero[data_frame$Logico == TRUE])

soma_falsos <- sum(data_frame$Numero[data_frame$Logico == FALSE])

print(soma_verdadeiros)

print(soma_falsos)

#7

mpg_vector <- mtcars$mpg

print(mpg_vector)

#8

str(mtcars)


#9

airquality_filtrado <- subset(airquality, !is.na(Ozone) & Month == 5)

linhas <- nrow(airquality_filtrado)
colunas <- ncol(airquality_filtrado)

print(paste( linhas))
print(paste( colunas))

#Operações com Arrays

#1

array_vazio <- array(NA, dim = c(3, 3))

array_vazio <- 1:9

dim(array_vazio) <- c(3, 3)

print(array_vazio)


#2

array1 <- array(1:9, dim = c(3, 3))
array2 <- array(9:1, dim = c(3, 3))

resultado <- array1 * array2

print(resultado)

#3

array_exemplo <- array(1:9, dim = c(3, 3))

indice_max <- which.max(array_exemplo)

linha_max <- (indice_max - 1) %/% nrow(array_exemplo) + 1
coluna_max <- (indice_max - 1) %% nrow(array_exemplo) + 1

print(paste("Índice de linha do valor máximo:", linha_max))
print(paste("Índice de coluna do valor máximo:", coluna_max))

#4

meu_array <- array(1:24, dim = c(3, 4, 2))
print(meu_array)


#5

meu_array <- array(1:24, dim = c(3, 4, 2))

# Aplicar sum() usando apply() com MARGIN = c(1, 2)
resultado_sum <- apply(meu_array, MARGIN = c(1, 2), sum)

# Exibir o resultado
print(resultado_sum)


#6


# Definir o array tridimensional
meu_array <- array(1:24, dim = c(3, 4, 2))

# Separar o conteúdo do array em duas matrizes
matriz1 <- meu_array[, , 1]
matriz2 <- meu_array[, , 2]

# Calcular o determinante de cada matriz
det1 <- det(matriz1)
det2 <- det(matriz2)

# Exibir os determinantes
print("Determinante da primeira matriz:")
print(det1)

print("Determinante da segunda matriz:")
print(det2)