from ejercicio1.mcd import mcd
from ejercicio2.mcm import mcm
from ejercicio4.palabra_frecuente import count_words, most_freq_word

# Ejemplo ejercicio 1 y 2
num1 = 18
num2 = 12

mcd12 = mcd(num1,num2)
mcm12 = mcm(num1,num2)

print(f"El MCD entre {num1} y {num2} es: {mcd12}")
print(f"El MCM entre {num1} y {num2} es: {mcm12}")

# Ejemplo ejercicio 3 y 4
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