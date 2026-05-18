
num1 = int(input("Digite o primeiro número (menor): "))
num2 = int(input("Digite o segundo número (maior): "))

print("\nNúmeros pares entre", num1, "e", num2, ":")

contador = num1

while contador <= num2:
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1
