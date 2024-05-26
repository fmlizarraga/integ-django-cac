# el MCM entre a y b se puede calcular a partir del MCD
# |a x b| / MCD

from ejercicio1.mcd import mcd

def mcm(a,b):
    return abs(a*b)/ mcd(a,b)
