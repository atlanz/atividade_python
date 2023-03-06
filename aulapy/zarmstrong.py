num = int(input("Digite um número inteiro: "))
soma = 0


while num > 0:
    digito = num % 10
    soma += digito ** num
    num //= 10


if soma == num:
    print(num,"é um número de Armstrong")
else:
    print(num, "não é um número de Armstrong")