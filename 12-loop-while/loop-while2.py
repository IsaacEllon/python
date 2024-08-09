import os

carros=[]
carro=input("Digite o novo nome do carro: ")

while carro!= "-1":
    carros.append(carro)
    carro=input("Digite o novo nome do carro: ")

os.system('cls')
for x in carros:
    print(x)