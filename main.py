from ejercicio1.mcd import mcd
from ejercicio2.mcm import mcm
from ejercicio4.palabra_frecuente import count_words, most_freq_word
from ejercicio5.get_int import get_int_recur, get_int_iter
from ejercicio6.Persona import Persona
from ejercicio7.Cuenta import Cuenta
from ejercicio8.Cuenta_Joven import Cuenta_Joven

# Ejemplo ejercicio 1 y 2
print("###### MCD - MCM ######")
num1 = 18
num2 = 12

mcd12 = mcd(num1,num2)
mcm12 = mcm(num1,num2)

print(f"El MCD entre {num1} y {num2} es: {mcd12}")
print(f"El MCM entre {num1} y {num2} es: {mcm12}")

# Ejemplo ejercicio 3 y 4
print("### Palábra más frecuente ###")
txt = '''
En matemáticas la sucesión de Fibonacci es una sucesión infinita
de números naturales
La sucesión comienza con dos números naturales
y a partir de estos
cada término es la suma de los dos anteriores
es esta relación de recurrencia lo que la define
'''

freqs = count_words(txt)
popular_word = most_freq_word(freqs)

print("Frecuencia de palabras:")
for word, freq in freqs.items():
    print(f"{word}: {freq}")

print(f"Palabra más frecuente: {popular_word[0]} - {popular_word[1]} veces")

# Ejemplo ejercicio 5
print("\n\n###### get_int (Iterativo) ######")
user_num = get_int_iter()

print(f"El valor ingresado fue: {user_num}")

print("###### get_int (Recursivo) ######")
user_num2 = get_int_recur()
print(f"El valor ingresado fue: {user_num2}")

# Ejemplo ejercicio 6
print("\n\n###### Persona ######")
persona1 = Persona()

my_name = input("Ingrese el nombre: ")
my_age = input("Ingrese la edad: ")
my_dni = input("Ingrese el DNI: ")

persona1.set_name(my_name)
persona1.set_age(int(my_age))
persona1.set_dni(int(my_dni))

persona1.mostrar()

# Ejemplo de Ejercicio 7
print("\n\n###### Cuenta ######")
persona2 = Persona(name="Juan Perez", age=30, dni=12345678)
cuenta = Cuenta(titular=persona2)

cuenta.mostrar()

cuenta.ingresar(500.50)
cuenta.mostrar()

cuenta.retirar(200)
cuenta.mostrar()

cuenta.retirar(1000)  # La cuenta puede estar en números rojos
cuenta.mostrar()

# Ejemplo de Ejercicio 8
print("\n\n###### Cuenta Joven ######")
persona3 = Persona(name="Carlos Rodriguez", age=23, dni=12345678)
cuenta_joven = Cuenta_Joven(titular=persona3, cantidad=1000.0, bonif=10)

cuenta_joven.mostrar()

cuenta_joven.ingresar(500)
cuenta_joven.mostrar()

cuenta_joven.retirar(200)
cuenta_joven.mostrar()

cuenta_joven.retirar(1500)
cuenta_joven.mostrar()

persona_mayor = Persona(name="Ana Garcia", age=30, dni=87654321)
cuenta_joven_no_valida = Cuenta_Joven(titular=persona_mayor, cantidad=1000.0, bonif=10)

cuenta_joven_no_valida.mostrar()
cuenta_joven_no_valida.retirar(300)