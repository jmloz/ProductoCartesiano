#ProductoCartesiano.
print("--------Ingrese los numeros del conjunto 1--------")
conjunto1 = []
for i in range(10):
    numero = input(f"Ingresa el número {i + 1} del conjunto 1: ")
    numero = int(numero)
    conjunto1.append(numero)

print("--------Ingrese los numeros del conjunto 2----------")
conjunto2 = []
for i in range(10):
    numero = input(f"Ingresa el número {i + 1} del conjunto 2: ")
    numero = int(numero)
    conjunto2.append(numero)

AxB = {(x, y) for x in conjunto1 for y in conjunto2}
BxA = {(x, y) for x in conjunto2 for y in conjunto1}

print("AxB: ",AxB)
print("\nBxA: ",BxA)
