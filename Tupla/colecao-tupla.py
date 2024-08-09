t_carros=("HRV","Golf","Argo")  #Tupla

l_carros=list(t_carros)
l_carros[2]="Focus" 
t_carros=tuple(l_carros)

#t_carros[2]="Focus"  #Tupla não suporta modificações diretamente

for x in t_carros:
    print(x)