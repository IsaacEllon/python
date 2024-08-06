x=1 #int
x="CFB cursos" #string
x=15.6 #float
x=False #bool
n1=5;n2=2;x=complex(n1,n2)

x=["Carro","Avião","Navio",1,58,3,True] #list / Array
x=("Carro","Avião","Navio",1,58,3,True) #Tupla - não pode modificar os itens da tupla
x=range(0,100) # cria um list de 0 a 100
x={  #Dict
    "canal":"CFB cursos",
    "curso":"Curso de Python",
    "nome":"Isaac"
}
x={5,7,4,5,4,8} # set - não repete valores
#print(x.real)
#print(x.imag)

print("Valor da variável: "+str(x))
#print("Valor da variável: "+str(x[0]))
print("Tipo: "+str(type(x)))