"""
texto="Curso de python "
palavra="python"

res=palavra.upper() in texto.upper() #in - verifica se tem a palavra python na var curso
print(res)
"""
"""
curso="Curso de Python"
canal="CFB Cursos"

res=curso+" do canal " +canal

print(res)
""" 
cidade="Eusébio"
dia=7
mes="Agosto"
ano=2024
canal="CFB Cursos"

#data=cidade+ ", "+str(dia)+" de "+mes+" de "+str(ano)
data="{}, {} de {} de {}\n \"{}\""
#\' \"" \n \r \t \b

print(data.format(cidade,dia,mes,ano,canal))


