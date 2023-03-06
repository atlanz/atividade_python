print("Digite 1 para somar, 2 para subtrair, 3 para dividir e 4 para multiplicar: ")
operacao = int(input("Informe: "))

if operacao == 1:
    a = float(input("Informe um valor"))
    b = float(input("Informe outro valor"))
    soma = (a+b)
    print(soma)

elif operacao == 2:
    a = float(input("Informe um valor"))
    b = float(input("Informe outro valor"))
    sub = (a-b)
    print(sub)

elif operacao == 3:
    a = float(input("Informe um valor"))
    b = float(input("Informe outro valor"))
    div = (a/b)
    print(div)

elif operacao == 4:
    a = float(input("Informe um valor"))
    b = float(input("Informe outro valor"))
    multi = (a*b)
    print(multi)






