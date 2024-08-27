num="Isaac"

if not type(num) is int:
    raise Exception("Somente números permitidos") #raise - gera uma execeção
else:
    print(num)
"""
x=10
try:
    print(x)

except: # except - executa apenas se o try retornar erro
    print("Erro no programa")
else:
    print("Tudo certo")
finally: # finally - executa se o try retornar erro ou não
    print("Fim do tratamento")
"""