# Si tenemos dos numeros a y b, donde a >= b:
# 1_ si b es 0, entonces el MCD es a
# 2_ si b no es 0, entonces el MCD de a y b es el mismo que
# el de b y el residuo de a / b (modulo de a y b)
# el MCD se calcula mediante un bucle realimentado que 
# repita (2) hasta que 1 sea cierto

def mcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
