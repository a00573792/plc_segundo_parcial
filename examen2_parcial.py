bebida = str(input("Dime tu tipo de bebida: puede ser café, té, o chocolate"))
hora = int(input("¿Qué hora del dia es?, de 1 a 24 horas y solo pon el número ejemplo 22"))
temperatura = int(input("¿Que temperatura tendra tu bebida en grados celcius"))

if temperatura< 50:
  print("Debe esperar a que se caliente la bebida")
elif temperatura>=50 and temperatura<= 70:
  print("Se puede servir de inmediato")
elif temperatura > 70:
  print("Bebida muy caliente, debe de esperar a que se enfrie")
if hora >= 6 and hora <= 11:
  print("Las bebidas se sirven mas rapido")
else:
  print("Espera el turno")
if bebida == "cafe" or "te" and hora >= 7 <= 9:
  print("te recomendamos una bebida caliente")
elif bebida == "té" or "chocolate" and hora >= 12 <= 14:
  print("te recomendamos una bebida fría")
