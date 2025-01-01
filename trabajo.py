"""Dada la categoría y sueldo de un trabajador, calcule el aumento correspondiente
teniendo en cuenta la categoría. Para la categoría 1 el aumento es del 15%, para
la categoría 2 es del 10%, para la categoría 3 es del 8%, para las demás categorías
es del 5%."""
while True:
    print(".....................")
    print("BIENVENIDO AL SISTEMA")
    print(".....................")
    print("categoria. 1")
    print("categoria. 2")
    print("categoria. 3")
    print("categoria. 4")
    print("salir.     5")
    op=int(input("Ingrese una opción:"))
    if op==1:
        sueldo1=float(input("Ingrese el sueldo del trabajador: "))
        print("Su aumento es: ",sueldo1*0.15)
        print("Sueldo: ",sueldo1+(sueldo1*0.15))
    elif op==2:
        sueldo2=float(input("Ingrese el sueldo del trabajador: "))
        print("Su aumento es: ",sueldo2*0.10)
        print("Sueldo: ",sueldo2+(sueldo2*0.10))
    elif op==3:
        sueldo3=float(input("Ingrese el sueldo del trabajador: "))
        print("Su aumento es: ",sueldo3*0.8)
        print("Sueldo: ",sueldo3+(sueldo3*0.8))
    elif op==4:
        sueldo4=float(input("Ingrese el sueldo del trabajador: "))
        print("Su aumento es: ",sueldo4*0.5)
        print("Sueldo: ",sueldo4+(sueldo4*0.5))
    elif op==5:
        break
    else:
        print("opción inválida")
