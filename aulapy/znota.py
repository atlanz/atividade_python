nota1 = float(input("Informe primeira nota"))
nota2 = float(input("Informe segunda nota"))
nota3 = float(input("informe a terceira nota")) 
media = (nota1+nota2+nota3)/3
if media >= 7:
    print("Passou com a nota: " +str(media))
else:
    print ("Não passou com a nota: " + str (media))