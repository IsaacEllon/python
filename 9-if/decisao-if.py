a=10
b=5
res=0
op="*"

if op=="+":
    res=a+b
if op=="-":
    res=a-b
if op=="*":
    res=a*b
if op=="/":
    res=a/b


print("Operação "+ op+ ": res = "+str(res))
print(str(a) + op + str(b) + " = " + str(res))