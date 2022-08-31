hora = input("Que horas são ? ")
if hora.isdigit() :
    hora = int(hora)
    if hora >= 0 and hora <= 11 :
        print("Bom dia !")
    elif hora >= 12 and hora <= 17 :
        print("Boa tarde !")
    elif hora >= 18 and hora <= 23 :
        print("Boa noite !")
    else :
        print("Insira uma hora válida !")

else :
    print("Insira uma hora válida !!")
