#Fatiamento

x = "0123456789"
print(x[0:2])
print(x[2:6])
print(x[4:-1])

#invertando uma string

palavra = input ('Palavra: ')
x = palavra[::-1]
print(x)

#verificando se a palavra e palindrome ou seja igual invertida
palavra = input ('Palavra: ')
if palavra == palavra[::-1]:
     print('%s é palindrome' %palavra)
else:
    print('%s não é palindrome' %palavra)

