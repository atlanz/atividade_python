nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))


if salario <= 1500:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.05

diferenca = novo_salario - salario

print(f"O novo salário de {nome} é R$ {novo_salario:.2f}")
print(f"A diferença entre o salário antigo e o novo é R$ {diferenca:.2f}")