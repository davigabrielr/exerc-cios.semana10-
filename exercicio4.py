numeros_pares = 0
numeros_inpares = 0
numeros_0 = 0
for numeros in range(10):
    numeros = int(input("digite um numero inteiro"))
    
    if numeros % 2 == 0:
        numeros_pares += 1
    
    if numeros % 2 != 0:
        numeros_inpares += 1
    
    if numeros == 0:
        numeros_0 += 1
print("numero de pares:", numeros_pares)
print("numero de inpares:", numeros_inpares)
print("numero de zeros:", numeros_0)
