
#isso aqui ja é sacanagem kkkkk:(
maior_idade = 0
contador_verde_preto = 0

olhos_azuis = 0
olhos_verdes = 0
olhos_castanhos = 0

cabelos_loiros = 0
cabelos_castanhos = 0
cabelos_pretos = 0

sexo_masc = 0
sexo_fem = 0

for i in range(15):
    print("\nPessoa", i+1)
    sexo = input("Sexo (M/F): ")
    olho = input("Olhos (A-azuis, V-verdes, C-castanhos): ")
    cabelo = input("Cabelos (L-loiros, C-castanhos, P-pretos): ")
    idade = int(input("Idade: "))

    if idade > maior_idade:
        maior_idade = idade

    if idade >= 18 and idade <= 35 and olho == "V" and cabelo == "P":
        contador_verde_preto += 1

    if olho == "A":
        olhos_azuis += 1
    elif olho == "V":
        olhos_verdes += 1
    elif olho == "C":
        olhos_castanhos += 1

    if cabelo == "L":
        cabelos_loiros += 1
    elif cabelo == "C":
        cabelos_castanhos += 1
    elif cabelo == "P":
        cabelos_pretos += 1

    if sexo == "M":
        sexo_masc += 1
    elif sexo == "F":
        sexo_fem += 1

total = 15
porc_azuis = olhos_azuis / total * 100
porc_verdes = olhos_verdes / total * 100
porc_castanhos = olhos_castanhos / total * 100

porc_loiros = cabelos_loiros / total * 100
porc_castanhos_cabelo = cabelos_castanhos / total * 100
porc_pretos = cabelos_pretos / total * 100

porc_masc = sexo_masc / total * 100
porc_fem = sexo_fem / total * 100

print("Maior idade:", maior_idade)
print("Qtd. entre 18 e 35 anos com olhos verdes e cabelos pretos:", contador_verde_preto)
print("Olhos Azuis:", porc_azuis, "%")
print("Olhos Verdes:", porc_verdes, "%")
print("Olhos Castanhos:", porc_castanhos, "%")
print("Cabelos Loiros:", porc_loiros, "%")
print("Cabelos Castanhos:", porc_castanhos_cabelo, "%")
print("Cabelos Pretos:", porc_pretos, "%")
print("Sexo Masculino:", porc_masc, "%")
print("Sexo Feminino:", porc_fem, "%")
