class Carro:
    velMax=0
    ligado=False
    cor=""
    def __init__(self, vm,li,c): #construtor
        self.velMax=vm
        self.ligado=li
        self.cor=c
    def mostrar(self):
        print("Velocidade máxima: " + str(self.velMax))
        print("Cor..............: " + self.cor)
        estado="Sim" if self.ligado else "não"
        print("ligado...........: " + estado)
        print("---------------------------------")
    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False
    def andar(self):
        if(self.ligado):
            print("Andando")
        else:
            print("Carro parado")

c1=Carro(200,False,"Preto")
c2=Carro(20,False,"Branco")
c3=Carro(350,False,"Vermelho")

c1.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()



