#imput
cliente= input("ingrese nombre del cliente :")
vendedor=input("ingrese nombre del vendedor:")
manteles =int (input("ingrese la cantidad de manteles:"))
pu=float(input("ingrese precio unitario:"))
adornos=int(input("ingrese la cant de adornos:"))
precio=float(input("ingrese el precio del adornos:"))

#procesing
total=(manteles*pu)
total2=(adornos*precio)
TOTAL3=(total+total2)

#ouput
print("##############################")
print("##  BOLETA ELECTRONICA      ##")
print("##  CASA HOGAR        ##")
print("# cliente:",cliente)
print("#vendedor:",vendedor)
print("#fecha=8/11/2019  Hora :8:50pm ")
print("#manteles:",manteles,"unidades")
print("#p.u:",pu)
print("#adornos:",adornos,"unidades")
print("#precio:",precio)
print("Total",total+total2)
print("#### GRACIAS POR SU COMPRA ###")
print("##############################")
