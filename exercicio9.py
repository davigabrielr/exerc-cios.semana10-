
jornal_A = 0
jornal_B = 0
jornal_C = 0

vez = 1
while vez <= 20:
    print("\nPessoa", vez)
    jornal = input("Qual jornal você lê? (A, B ou C): ")

    if jornal == "A":
        jornal_A = jornal_A + 1
    elif jornal == "B":
        jornal_B = jornal_B + 1
    elif jornal == "C":
        jornal_C = jornal_C + 1
    else:
        print("Opção inválida, não será contada.")

    vez = vez + 1

total = jornal_A + jornal_B + jornal_C
porc_A = jornal_A / total * 100
porc_B = jornal_B / total * 100
porc_C = jornal_C / total * 100


if porc_A <= porc_B and porc_A <= porc_C:
    print("Jornal A:", porc_A, "%")
    if porc_B <= porc_C:
        print("Jornal B:", porc_B, "%")
        print("Jornal C:", porc_C, "%")
    else:
        print("Jornal C:", porc_C, "%")
        print("Jornal B:", porc_B, "%")

elif porc_B <= porc_A and porc_B <= porc_C:
    print("Jornal B:", porc_B, "%")
    if porc_A <= porc_C:
        print("Jornal A:", porc_A, "%")
        print("Jornal C:", porc_C, "%")
    else:
        print("Jornal C:", porc_C, "%")
        print("Jornal A:", porc_A, "%")

else:
    print("Jornal C:", porc_C, "%")
    if porc_A <= porc_B:
        print("Jornal A:", porc_A, "%")
        print("Jornal B:", porc_B, "%")
    else:
        print("Jornal B:", porc_B, "%")
        print("Jornal A:", porc_A, "%")
