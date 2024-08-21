#Chave/Key - Valor/Value
carro={
    "Fabricante":"Honda", 
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
} #dictionary

carro["Cambio"]="Automatico"
carro.pop("Cambio") #del carro["Cambio"]


fab=carro["Fabricante"]  #fab=carro.get("Fabricante")

carro["Cor"]="Preto"

print("Tamanho do Dictionary: "+ str(len(carro)))

if "Modelo" in carro:
    print("Sim, Modelo é uma chave \n")

for c,v in carro.items():
    #print(x) #Chave
    print(c + ": " + v) #Valor
