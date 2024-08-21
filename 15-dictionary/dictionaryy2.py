"""
carros={
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro2":{
        "Fabricante":"Volkswagem",
        "Modelo":"Golf"
    },
    "Carro3":{
        "Fabricante":"Ford",
        "Modelo":"Focus"
    } 
}
"""

Carro1={    
    "Fabricante":"Honda",
    "Modelo":"HRV"
    }
Carro2={
    "Fabricante":"Volkswagem",
    "Modelo":"Golf"
    }
Carro3={
    "Fabricante":"Ford",
    "Modelo":"Focus"
    } 

carros={
    "C1":Carro1,
    "C2":Carro2,
    "C3":Carro3,
}


print(carros["C1"]["Modelo"])