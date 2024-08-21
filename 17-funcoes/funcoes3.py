valores=[1,5,3,2]

def somar(num):
    r=0
    for n in num:
        r+=n
    return r

res=somar(valores)

print(str(valores) + ": soma = " + str(res))


