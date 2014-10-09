#Brincando com marcadores
#Comando ( /n ) dentro do print server para pular uma linha para fica melhor de ler
#Variaveis
a = 10
texto = 'Frutas'
pi = 3.1415

#prints
print('O numero é',a)
print ('O numero', a , 'é muito legal se for nota')
#Marcadores
print(':::Logo abaixo primeiro exemplo de marcadores ::: \n')
print('O numero %d é muito legal se for nota' %a)

#Tipos de Marcadores
# %d - numeros decimais
# %s - strings
# %f - para numeros float ou seja numeros quebrados como PI ( 3.1415)

#usando os tipos definidos a cima

#tipo %d
print(':::Logo abaixo exemplo do marcador tipo decimal::: \n')
print('O numero %d é muito legal se for nota' %a)
#tipo %s
print(':::Logo abaixo exemplo do marcador tipo string::: \n')
print ('Comer %s é bom para saude ' %texto)
#tipo %f
print(':::Logo abaixo exemplo do marcador tipo float::: \n')
print('O valor de PI %f' %pi)
#Tratando o numero de casas decimais com marcador tipo float
print('O valor de PI com 2 casas %.2f' %pi)

