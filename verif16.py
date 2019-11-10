#Calculadora 17
#este programa nos ayudara a calcular en cuanto tiempo acabaran los obreros una obra
obreros,avancepersonal,obra=0,0.0,0
#calculadora
obreros=20
avancepersonal=1/5
obra=1
dias=(obreros*avancepersonal*obra)
#mostrar dato
print("el valor de obreros=",obreros)
print("el valor de avancepersonal=",avancepersonal)
print("el valor de dias=",dias)
#verificador
eficientes=(dias<4)
print("son igual de eficientes que los primeros obreros?:",eficientes)
#fin
