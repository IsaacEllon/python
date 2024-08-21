import random
import os

erro=0
sorteado=random.randrange(0,100)
#print(str(sorteado))
jogador=int(input("Digite seu número: "))

while(sorteado!=jogador):
    os.system("cls")
    if(sorteado>jogador):
        print("ERRO, o número é maior")
    elif(sorteado<jogador):
        print("ERRO, o número é menor")
    erro+=1
    jogador=int(input("Digite seu número: "))

print("Número "+ str(jogador) + ", você acertou em " + str(erro+1) + " tentativas")
50