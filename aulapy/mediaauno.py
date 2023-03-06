nota = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))

media = (nota + nota2)/2

if media >= 6:
    print("Passou" + str(media))
else:
    print ("Reprovou")
    
          