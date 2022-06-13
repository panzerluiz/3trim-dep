par = 0
imp = 0
for x in range(10):
    if int(input("Digite um numero: ")) % 2 == 0:
        par += 1
    else:
        imp+= 1
print(f"Pares: {par}\nÍmpares: {imp}")