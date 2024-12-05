capital = float(input("Ingresa el capital inicial: "))
tasa_interes = float(input("Ingresa la tasa de interes (en %): ")) / 100
tiempo = float(input("Ingresa el tiempo (en años): "))
tipo_interes = input("¿Deseas calcular interés simple (S) o compuesto (C)?").upper()
if tipo_interes == 'S':
    interes_simple = capital * tasa_interes * tiempo
    monto_total = capital + interes_simple
    print(f"interés simple: {interes_simple:.2f}. Monto total: {monto_total:.2f}.")
elif tipo_interes == 'C':
    monto_total = capital * (1 + tasa_interes) ** tiempo
    interes_compuesto = monto_total - capital
    print(f"Interes compuesto: {interes_compuesto:.2f}. Monto total: {monto_total:.2f}.")
else:
    print("Tipo de interes no valido. Por favor, Ingresa 'S' o 'C'.")





