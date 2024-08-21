valores=[1,5,3,2]

def somar(*num):
    r=0
    for n in num:
        r+=n

    print("Soma = " + str(r))
    print("Youtube.com\n")

def carros(c="Golf"):
    print("Modelo: " + c)

carros("HRV")

somar(valores)


"""
def textos(*txt):
    for t in txt:
        print(t)

textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")
"""