#Brincando com entrada de dados

#print normal
nome = 'Zumbi'
print (nome)
#print com entrada de dados
nome = input('Digite o seu nome:') #o input sempre retorna uma string
print (nome)
#testando a soma de valores com string para ver o resultado
n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')
print (n1 + n2) # ele vai junta os 2 valores e nao somar
#somando os 2 numeros , basta converte
n1 = int(input('Digite um numero: ')) #usando a função int() para muda de string para inteiro
n2 = int(input('Digite outro numero: '))
print (n1 + n2)
#passando para float ou seja numeros decimais
n1 = float(input('Digite um numero: ')) #usando a função float() para muda de string para decimal
n2 = float(input('Digite outro numero: '))
print (n1 + n2)
