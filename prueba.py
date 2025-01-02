import math
while True:
    print("----------------------")
    print("CALCULADORA MATEMÁTICA")
    print("----------------------")
    print("SUMA                .1")
    print("RESTA               .2")
    print("DIVISIÓN            .3")
    print("MULTIPLICACIÓN      .4")
    print("POTENCIA            .5")
    print("RAÍZ CUADRADA       .6")
    print("RAÍZ CÚBICA         .7")
    print("SALIR               .8")
    print("----------------------")
    op=int(input("Ingrese una opción:"))
    if op==1:
        a=float(input("Ingrse el primer número:"))
        b=float(input("Ingrese el segundo número:"))
        print(a+b)
    elif op==2:
        c=float(input("Ingrese el primer número:"))
        d=float(input("Ingrese el segundo número:"))
        print(c-d)
    elif op==3:
        e=float(input("Ingrese el primer número:"))
        f=float(input("Ingrese el segundo número:"))
        print(e/f)
    elif op==4:
        g=float(input("Ingrese el primer número:"))
        h=float(input("Ingrese el segundo número:"))
        print(g*h)
    elif op==5:
        i=float(input("Ingrese la base:"))
        j=float(input("Ingrese el exponente:"))
        print(pow(i,j))
    elif op==6:
        k=float(input("Ingarese un número:"))
        print(math.sqrt(k))
    elif op==7:
        l=float(input("Ingrese un número:"))
        print(math.cbrt(l))
    elif op==8:
        break
    else:
        print("Opción incorrecta, ingrese otra opción")
        print("......................................")


