#imput
cliente= input("ingrese nombre del cliente :")
vendedor=input("ingrese nombre del vendedor:")
galletas =int (input("ingrese la cantidad de galletas:"))
pu=float(input("ingrese precio unitario:"))
yogurt=int(input("ingrese la cant de yogurt:"))
precio=float(input("ingrese el precio del yogurt"))

#procesing
total=(galletas*pu)
total2=(yogurt*precio)

#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##   BODEGA LIBERTAD        ##")
print("# cliente:",cliente)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#galletas:",galletas,"unidades")
print("#p.u:",pu)
print("#yogurt:",yogurt,"unidades")
print("#precio:",precio)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
