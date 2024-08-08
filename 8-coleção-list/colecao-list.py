carros=["HRV", "Golf", "Argo", "Focus"]
carros.append("Fit")  #append - adição de novos itens a lista
carros.append("Fusion")
carros.append("Polo")

carros2=["Fusca", "147","Brasilia,","Celta"]
#carros2=list(carros)  #  carros2 vai receber toda a lista carros

carros3=carros+carros2

#del carros[2]  #del - consegue remover por indexação 
#carros.remove("Fusion")  #remove - remove itens da lista
#carros.pop()  #pop - remove o ultímo item
#carros.clear()  #clear - remove a lista inteira

print(str(len(carros3))+ " carros na lista") # len - informa a quantidade

print(carros3)