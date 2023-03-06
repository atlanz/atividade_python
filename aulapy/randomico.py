import random

pc = random.randrange(0,2)
print(" Digite 0 para pedra, 1 para papel e 2 para tesoura. ")
usuario = int(input(" Digite sua jogada querido usuario: "))
print ("Eu joguei", pc)

if usuario == pc:
    print (" Empate ")
elif usuario == 0 and pc == 2:
    print(" Parabens você venceu")
elif usuario == 1 and pc == 0:
    print(" Parabens você venceu")
elif usuario == 2 and pc == 1:
    print(" Parabens você venceu")

elif pc == 0 and usuario == 2:
    print(" Eu venci, hahahaha")
elif pc == 1 and usuario == 0:
    print(" Eu venci, hahahaha")
elif pc == 2 and usuario == 1:
    print(" Eu venci, hahahaha")