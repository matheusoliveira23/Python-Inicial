#aplicação teste do banco
from gm import Cliente
from gm import Conta
from gm import ContaEspecial
print('===BEM VINDO - BANCO GM CRED===')
gustavo = Cliente('gustavo marinho','9954-3075')
larissa = Cliente('larissa peixoto','9650-1323')
print('Nome: %s. Telefone: %s.' % (gustavo.nome, gustavo.telefone))
print('Nome: %s. Telefone: %s.' % (larissa.nome, larissa.telefone))

conta_g = Conta([gustavo],3,1000)
conta_gl = ContaEspecial([larissa,gustavo],4,500,1000)

conta_g.resumo()
conta_gl.resumo()
conta_g.saque(50)
conta_gl.deposito(300)
conta_g.saque(190)
conta_gl.deposito(95.15)
conta_gl.saque(1500)
conta_g.extrato()
conta_gl.extrato()
