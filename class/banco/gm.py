#Criando as classes do banco
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
class ContaEspecial(Conta):
    def __init__(self,clientes,numero,saldo = 0,limite = 0):
        Conta.__init__(self,clientes,numero,saldo)
        self.limite = limite
    def resumo(self):
        print('CC numero: %s Saldo: %10.2f' %(self.numero,self.saldo))      
    def saque(self,valor):
        if self.saldo  >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque',valor])
    def deposito(self,valor):
            self.saldo += valor
            self.operacoes.append(['Deposito',valor])
    def extrato(self):
        print('Extrato CC N° %s' %self.numero)
        for op in self.operacoes:
            print('%10s %10.2f' %(op[0],op[1]))
            print('%10s %10.2f\n' %('saldo=', self.saldo))

