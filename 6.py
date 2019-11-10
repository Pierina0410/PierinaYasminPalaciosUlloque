#imput
cliente= input("ingrese nombre del cliente :")
vendedor=input("ingrese nombre del vendedor:")
muebles =int (input("ingrese la cantidad de muebles:"))
pu=float(input("ingrese precio unitario:"))
sillas=int(input("ingrese la cant de sillas:"))
precio=float(input("ingrese el precio del sillas:"))

#procesing
total=(muebles*pu)
total2=(sillas*precio)
TOTAL3=(total+total2)

#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##  MUEBLERIA COMODIDAD        ##")
print("# cliente:",cliente)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#muebles:",muebles,"unidades")
print("#p.u:",pu)
print("#sillas:",sillas,"unidades")
print("#precio:",precio)
print("TOTAL:",total)
print("Total",total+total2)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
