#Este codigo vale 1 decima
a = 1
value = input('Ingrese un valor ')
value = int(value)

while a == 1:
    for i in range(1,value+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1

    if conta == 2:
       print(f'{i} Es un primo')
       print("\n")
    else:
       print(f'{i} No es un primo')
       print("\n")

    print('Presione 1 para continuar')
    a = input()
    a = int(a)

    if a != 1:
        break

    value = input('Ingrese un valor ')
    value = int(value)
