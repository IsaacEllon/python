curso="Curso de python "



#print(curso[0:5])
#print(curso.strip()) #strip - retira os espaços
#print(curso.lower().strip()) #lower - deixa faz a conversão para minusculo
#print(curso.upper()) #upper - converte tudo em maiusculo 
#print(curso.replace("python", "C#")) #replece - substitui uma string ou caracter por outra string ou caracter.
a=curso.split(" ") # dentro do parêntese fica o indicador de corte, nesse caso especifico é o espaço
print(a[2]) #split - quando tiver um espaço ele vai fazer um corte
print("Tamanho: " + str(len(curso))) #len - informa o tamanho