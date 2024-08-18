#Chave/Key - Valor/Value
carro={
    "Fabricante":"Honda", 
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
} #dictionary

fab=carro["Fabricante"]  #fab=carro.get("Fabricante")

carro["Cor"]="Preto"

for x in carro:
    #print(x) #Chave
    print(carro[x]) #Valor
