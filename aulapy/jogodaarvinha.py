import random

acertou = False
narvores = 50
tentativas = 0
esconde = 0

print("1 - facil")
print("2 - medio")
print("3 - dificil")
dificuldade = int(input("Informe a dificuldade: "))


if dificuldade == 1:
    tentativas = 15
    
elif dificuldade == 2:
    tentativas = 10
    
else:
    tentativas = 5


esconde = random.randint(0, 50)
for x in range(tentativas + 1):
    nt = int(input("Informe um número: "))
    
    if nt > esconde:
        print("Está mais à esquerda.")
    elif nt < esconde:
        print("Está mais à direita.")
    else:
        acertou = True
        break
        
if acertou == False:
    print("Perdeu.")
else:
    print("Ganhou.")