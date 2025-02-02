#Verificação de Palíndromo:
#Escreva um programa que verifique se uma string é um palíndromo (lê-se da mesma forma de trás para frente)
letura = str(input("Digite a palavra a ser verificada se ou não um palíndromo: "))
reverse = ''.join(reversed(letura))
# Aqui está o que acontece:
# reversed(texto) cria um iterador que gera os caracteres de texto na ordem inversa.
# ''.join(...) pega esses caracteres e os une em uma nova string. 
# As aspas simples '' são usadas como um delimitador vazio, ou seja, 
# os caracteres serão unidos sem nenhum separador entre eles.
# Se você não usar as aspas simples, a função .
# join() não saberá como juntar os caracteres, 
# e o código não funcionará corretamente. 
# É como se as aspas simples dissessem ao 
# Python: "Pegue todos os caracteres invertidos e os una em uma nova string, 
# sem nenhum separador entre eles".
if letura == letura and letura == reverse:
    print("Isso é um palíndromo")
else:
    print("Isso não é um palíndormo")