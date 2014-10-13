#Empresa de telefonia kkkkk fazendo os exercicio do curso

#perguntando ao cliente
minutos = int(input('Quantos minutos voce usou:'))

#calculando
if minutos < 200:
    print('Sua tarifa e de $RS0,20 por minuto')
    preço = 0.20
elif minutos > 200 and minutos < 400:
    print('Sua tarifa e de $RS0,18 por minuto')
    preço = 0.20
elif minutos >= 800:
    preço = 0.8
    print('Sua tarifa e de $RS0,8 por minuto')
else:
    preço = 0.15
    print('Sua tarifa e de $RS0,15 por minuto')

print('O valor da sua conta $RS %.2f' %(minutos * preço ))
