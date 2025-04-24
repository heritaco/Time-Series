import numpy as np

def modulo_raices(p1=0, p2=0, p3=0, p4=0, p5=0, p6=0, p7=0, p8=0, p9=0, p10=0, p11=0, p12=0):

    coef = np.zeros(13)

    coef[0] = p12     # x^12
    coef[1] = p11     # x^11
    coef[2] = p10     # x^10
    coef[3] = p9      # x^9
    coef[4] = p8      # x^8
    coef[5] = p7      # x^7
    coef[6] = p6      # x^6
    coef[7] = p5      # x^5
    coef[8] = p4      # x^4
    coef[9] = p3      # x^3
    coef[10] = p2     # x^2
    coef[11] = p1     # x^1
    coef[12] = 1      # x^0
    
    raices = np.roots(coef) # Raices del polinomio
    modulo = np.abs(raices) # Módulo de las raíces
    estacionario = np.all(modulo > 1) # Verificar si todas las raíces están fuera del círculo unitario
    
    print("Raíces del polinomio característico:", raices)
    print("\nMódulo de las raíces:", modulo)
    print("\n¿Las raíces están fuera del circulo unitario? ", estacionario)
    
    return