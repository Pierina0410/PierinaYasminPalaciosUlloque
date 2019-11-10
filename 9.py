#imput
cliente= input("ingrese nombre del cliente :")
vendedor=input("ingrese nombre del vendedor:")
juguetes=int (input("ingrese la cantidad de juguetes:"))
pu=float(input("ingrese precio unitario:"))

#procesing
total=(juguetes*pu)

#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##   JUGUETERIA DIVERSION      ##")
print("# cliente:",cliente)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#juguetes:",juguetes ,"docenas")
print("#p.u:",pu)
print("TOTAL:",total)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
