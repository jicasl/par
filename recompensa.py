gasto =float(input("Ingresa el total de tus compras: "))
recompensa = 0
if gasto > 100:
    recompensa = gasto * 0.10
elif 50 <= gasto <= 100:
    recompensa =gasto * 0.05
print(f"Tu recompensa es: {recompensa:.2f}.")
