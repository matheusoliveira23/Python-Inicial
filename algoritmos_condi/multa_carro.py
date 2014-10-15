#Algoritmo para multar os carros kkkkk 'So uma brincadeira

#Pegando os valores
velocidade = int(input('Digie a velocidade do carro "Valor inteiro":'))  #vms tentar pegar um float?
if velocidade > 110:
    print('Voce foi multado :(')
    multa = (velocidade - 110)*5
    print('Que pena voce vai pagar %d Reais de multa'%multa)
else:
    print('Esta tudo OK! , pode continuar')
    
