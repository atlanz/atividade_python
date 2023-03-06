print ("Os carros disponiveis são: ")
print ("1-BMW 2-AUDI 3-FIAT 4-FERRARI ")

tpcarro = int(input("Selecione o carro:" ))

comb = int(input("Qual o combustivel, 1-gasolina, 2-alcool? "))

if tpcarro == 1:
    valorgasolina = float(9.8)
    valoralcool = float(8.9)
    
elif tpcarro == 2:
    valorgasolina = float(12.8)
    valoralcool = float(10.9)

elif tpcarro == 3:
    valorgasolina = float(26.8)
    valoralcool = float(24.9)
    
elif tpcarro == 4:
    valorgasolina = float(13.8)
    valoralcool = float(12.9)
    
if comb == 1:
    valordecalc = valorgasolina
else:
    valordecalc = valoralcool
    
    
fourdoors = input("O carro possui mais de 4 portas? 1 pra sim, 2 pra não: ")
morepeoples = input("Mais de duas pessoas iram viajar? 1 pra sim, 2 pra não: ")
bag = input("Possui bagageiro? 1 pra sim, 2 pra não: ")


if fourdoors == "1":
    valordecalc = valordecalc - 0.5
    
if morepeoples == "1":
    valordecalc = valordecalc - 1.2
    
if bag == "1":
    valordecalc = valordecalc - 0.2
    
print ("A quantidade de litros por kilometro a ser gasto é:" )
print (str(valordecalc))