#Repetições


#forma simples
print ('====Forma Simples===')
print(1)
print(2)
print(3)
#forma com variavel
print ('====Forma Variavel===')
x = 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
#usando o while
print ('====Forma While===')

x = 1
while x <= 3:
    print(x)
    x = x + 1
#imprimindo de 1 ate o numero digitado pelo usuario
print('==imprimindo de 1 ate o numero digitado pelo usuario==')
numero = int(input('Digite um numero: '))
contador = 1

while contador <= numero:
    print(contador)
    contador = contador + 1
#imprimindo os numeros par
print('==imprimindo os numeros par==')
numero = int(input('Digite um numero: '))
contador = 0

while contador <= numero:
        print(contador)
        contador = contador + 2
        

