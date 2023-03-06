print("Olá, seja bem-vindo a loja de ovos de páscoa da dona maria <3 ")
print("Vamos prosseguir com as especificações para a confecção de seu(s) ovo(s) de páscoa ")


valorfinal = 0


print ("Indique qual deve ser o tamanho do(s) ovo(s) ")
tamanho = int(input("1-Pequeno, 2-Medio, 3-Grange: "))

if tamanho == 1:
    precotamanho = float(7.80)
if tamanho == 2:
    precotamanho = float(12.90)
if tamanho == 3:
    precotamanho = float(23.95)


print("Temos os seguintes sabores: 1-Chocolate preto, 2-Chocolate branco, 3-Chocolate ao leite ")
sabor = int(input("Informe qual o sabor escolhido: "))
outrsabor = input("Gostaria de adcionar outro sabor? ")
if outrsabor == "sim":
    saboradd = input("Qual saboria gostaria de adicionar alem do anteriormente selecionado? ")
    

    
    
    

add = int(input("Gostaria de adicionais? temos: 1- KitKat e 2-MM's "))
outroadd = input("Gostaria de colocar o outro adicional tambem? 1-sim, 2-não")
if outroadd == "sim":
    add = input("Voce gostaria que seu ovo de páscoa possuisse kk e mm's, certo?")
if add == "sim":
    add = add + outroadd
    
gift = input("Esse ovo seria um presente?")
if gift == "sim":
    valorfinal