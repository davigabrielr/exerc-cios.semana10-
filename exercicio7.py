
num1 = int(input("Digite o primeiro número (menor): "))
num2 = int(input("Digite o segundo número (maior): "))

print("\nNúmeros pares entre", num1, "e", num2, ":")

for i in range(num1, num2 + 1):
    if i % 2 == 0:   
        print(i)
