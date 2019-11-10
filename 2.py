#calculadora2
#esta calculadroa realiza el calculo de como hallar la energia

#declaracion de variables
masa,velocidad_de_la_luz=0,0.0

#calculadora
masa=5
velocidad_de_la_luz= 3*(10**14)
energia=(masa*velocidad_de_la_luz*velocidad_de_la_luz)

#mostrar datos
print ("el valor de la masa =",masa)
print("el valor de velocidad_de_la_luz = ",velocidad_de_la_luz)
print("el valor de energia =",energia)
#verificador
energia_baja= (energia<1000)
print("energia_baja?:",energia_baja)
#fin

