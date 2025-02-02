#Fatorial:
#Crie uma função que calcule o fatorial de um número inteiro positivo fornecido pelo usuário.
leitura = (int(input("Digite um numero para ser fatorado: " )))
j = 1
k = leitura - (leitura-1)
i = leitura
while j < i:
    leitura = leitura*j
    j +=1
print("Esse numero em fatorial é:",leitura)
