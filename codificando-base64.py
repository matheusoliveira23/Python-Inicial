#Codificando uma string na base64

import base64

#criando variaveis
texto_codec = 'Python ta cada vez mais legal'

#codificando na base64

codigo = base64.b64encode(b'texto_codec') #comando para codificar a frase
print('Sua frase codificada é:')
print(codigo) #imrpimindo frase codificada
print('Sua frase normal é:')
print(texto_codec) #imrpimindo frase normal
