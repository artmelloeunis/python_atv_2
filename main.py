from math import *

cateto_1 = int(input("Primeiro cateto: "))
cateto_2 = int(input("Segundo cateto: "))
hipotenusa = int(input("Hipotenusa: "))

if(cateto_1 > 0 and cateto_2 > 0):
    semiperimetro = (hipotenusa + cateto_1 + cateto_2) / 2
    area_total = sqrt(semiperimetro * (semiperimetro - hipotenusa) * (semiperimetro - cateto_1) * (semiperimetro * cateto_2))

    print("É um triangulo! Área do triângulo: {:.2f}.".format(area_total))
elif(hipotenusa > (cateto_1 + cateto_2)):
    print("\nNão é um triangulo!")