segundos = input("Ingrese la cantidad de segundos: ")
segundos = int(segundos)

minutos = segundos // 60
segundos_resto = segundos % 60

horas = minutos // 60
minutos_resto = minutos % 60

print("tiempo: ", horas, "horas,", minutos_resto, "minutos,", segundos_resto, "segundos")