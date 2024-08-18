carros=[
    ["Modelo", "HRV"],
    ["Fabricante", "Honda"],
    ["Ano",2016]
] #matriz

carros.append(["Cor", "Prata"])
carros[2][1]=2019

print(carros[0][1])

for l,c in carros:
    print(l + " | "+ str(c) )