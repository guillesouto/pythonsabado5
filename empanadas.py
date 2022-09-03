print("***MENU***")
print("1. agregar 1 empanada")
print("2. Mostrar Empanada")
print("3. SALIR")
opcion=100
#DATOS EMPANADA
#SABOR
#INGREDIENTES (x3)
#PRECIO FABRICACION
#PRECIO VENTA

empanadas=[]
ingredientes=[]

while(opcion != 3):
    empanada= {}
    opcion = int(input("Digite una opcion: "))
    if(opcion == 1):
        empanada['Sabor']=input("Digite el sabor de la empanada: ")
        empanada["ingredientes"]=[]
        for i in range(3):
            ingredientes.append(input("Digite el nombre del ingrediente "))
        empanada['ingredientes']= ingredientes
        empanada['precioFabricacion']=input("Digite el precio de fabricacion: ")
        empanada['precioVenta']=input("Digite el precio de venta por empanada: ")
        empanadas.append(empanada)
        print("agregando empanada")
    elif(opcion ==2):
        print(empanada)
        print("mostrando empanada")
    else:
        print("digite una opcion valida")
else:
print('fin')


    