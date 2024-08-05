num1=num2=res=0
canal="CFB cursos"  #Escopo global

def cn():
    global curso #Escopo local, mas para acessar ela como global, basta definir com tal.
    curso="Curso de python" #Tem que ser inicializada ma linha seguinte
    print(curso)

cn()