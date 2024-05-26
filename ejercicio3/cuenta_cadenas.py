# implemente una funcion para hacer lo que se pide
# paso la cadena de caracteres a todo minusculas
# las corto y las gueardo temporalmente en una lista
# esa lista la itero y compruebo si la palabra ya existe
# si no existe se agrega una clave con el nombre de esa palabra
# con el valor 1
# si ya existe, solo se incrementa el valor
# al final, la funcion devuelve el diccionario

def count_words(string: str):
    words = string.lower().split()
    wordcount = {}
    
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    
    return wordcount

# ejemplo
txt = '''
Escribir una función que calcule el máximo común divisor entre dos números
Escribir una función que calcule el mínimo común múltiplo entre dos números
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia)
Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia)
Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva
'''

freqs = count_words(txt)

print("Frecuencia de palabras:")
for word, freq in freqs.items():
    print(f"{word}: {freq}")