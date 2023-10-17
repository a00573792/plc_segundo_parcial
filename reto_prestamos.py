https://replit.com/@ErickSaldana1/calculadora-de-prestamos?v=1

dinero = int(input("¿Cuanto dinero quieres que te preste?"))
interes = int(input("Taza de interes anual"))
tiempo = int(input("Plaza del prestamo en años"))
    
if interes<= 5 and tiempo<=5:
             print("Prestamo de bajo riesgo")
elif interes> 5 or tiempo>5:
             print("Prestamo de riesgo moderado")
else:
             print("Prestamo de alto riesgo")
