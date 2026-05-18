
dentro = 0  
fora = 0   

for vez in range(10):
    numero = int(input("Digite um número: "))

    if numero >= 10 and numero <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print("Quantidade dentro do intervalo [10,20]:", dentro)
print("Quantidade fora do intervalo:", fora)
