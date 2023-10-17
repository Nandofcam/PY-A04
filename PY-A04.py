# (PY-A04) Escreva uma função em Python que recebe dois números como argumentos e retorna o maior entre eles:

num_1 = float(input("Insira o primeiro número: "))
num_2 = float(input("Insira o segundo número: "))

# a) Implemente a função com o nome "maior_numero" e utilizando condicionais:

def maior_numero(num_1, num_2):
    if num_1 > num_2:
        print("O primeiro número é maior que o segundo!")
    elif num_1 == num_2:
        print("Ambos os números são  iguais!")
    else:
        print("O segundo número é maior que o primeiro!")

maior_numero(num_1, num_2)

# b) Implemente a mesma função, porém utilizando a função "max":

def maior_numero_max(num_1, num_2):
    print(f"O maior número é o {max(num_1, num_2)}")

maior_numero_max(num_1, num_2)