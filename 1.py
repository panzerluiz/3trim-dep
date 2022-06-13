#entrada de dados
n1=int(input("Digite um número"))
n2=int(input("Digite um número"))
n3=int(input("Digite um número"))
n4=int(input("Digite um número"))
n5=int(input("Digite um número"))
#processamento de dados
if n1>n2 and n1>n3 and n1>n4 and n1>n5:
#saída de dados
    print(n1)
elif n2>n1 and n2>n3 and n2>n4 and n2>n5:
    print(n2)
elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
    print(n3)
elif n4>n1 and n4>n3 and n4>n2 and n4>n5:
    print(n4)
else:
    print(n5)
