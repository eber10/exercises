""""imprimir la siguiente figura
         *
        ***
       *****
      *******
     *********
      *******
       *****
        ***
         * 
"""
n=int(input("Ingresse el número de filas: "))
mitad=n//2
for i in range(0,mitad+1):
    for j in range(0,mitad-i):
        print(" ", end="")
    for j in range(0,2*i+1):
        print("*", end="")
    print()
for i in range(mitad-1,-1,-1):
    for j in range(0,mitad-i):
        print(" ", end="")
    for j in range(0,2*i+1):
        print("*",end="")
    print()