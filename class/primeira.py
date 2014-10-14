#brincando com class

class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def muda_canal_para_baixo(self):
        self.canal -= 1
    def muda_canal_para_cima(self):
        self.canal += 1
    def ligar_tv(self):
        self.ligada = True
    def desliga_tv(self):
        self.ligada = False
