numeros = [1,2,3,4]
numeros2=[]
for i in numeros:
    numeros2.append(i*2)

numeros3= list(map(lambda i:i*2, numeros))

print(numeros)
print(numeros2)
print(numeros3)

print("-------------------------")

numeros4=[1,2,3,4]
numeros5=[1,2,3]

resultado=list(map(lambda x,y:x+y,numeros4,numeros5))
print(resultado)
