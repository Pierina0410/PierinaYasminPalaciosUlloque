#Calculadora 11
#este programa nos ayudara a calcular el numero de litros de agua que toma una familia durante una semana
litros_al_dia, numerodeintegrantes,dias = 0,0,0
#calculadora
litros_al_dia=5
numerodeintegrantes=8
dias=7
litrostotal=(litros_al_dia*numerodeintegrantes*dias)
#mostrar datos
print("el valor de litros_al_dia=",litros_al_dia)
print("el valor de numerodeintegrantes=",numerodeintegrantes)
print("el valor de dias=",dias)
print("el valor de litrostotal=",litrostotal)
#verificador
jarra=(litrostotal==2)
print("toma mas de una jarra de agua?:",jarra)
#fin
