"método de burbuja"
tam=int(input("Ingrese el tamaño del arreglo: "))
arr=[0]*tam
for i in range(tam):
    arr[i]=int(input(f"Ingrese el valor {i+1}:"))
for i in range(tam):
    print(arr[i],end=" ")
print("\nvalores ordenados")
for i in range(tam-1):
    for j in range(i+1,tam):
        if arr[i]>arr[j]:
            aux=arr[i]
            arr[i]=arr[j]
            arr[j]=aux
for i in range(tam):
    print(arr[i],end=" ")

    