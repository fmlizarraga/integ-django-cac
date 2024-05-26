# Para la solucion iterativa utilizo un bloque while True
# Este se repite infinitamente mientras se capturen excepciones
# Cada vez que se captura la excepcion, se itera otra vez
# Cuando el bloque try se ejecuta correctamente se devuelve el valor
# terminando la funcion y el ciclo while de una vez
# Este método es mas eficiente porque no agrega llamadas al stack
# reitera utilizando el mismo contexto
# pero es ligeramente menos legible por tener un nivel extra de anidacion

def get_int_iter():
    while True:
        try:
            user_in = input("Ingrese un numero entero: ")
            my_number = int(user_in)
        except ValueError:
            print("Debe ingresar un numero entero valido!")
        else:
            return my_number

# Paara la solucion recursiva se llama a un bloque try exept
# igual que antes, pero cuando se captura la excepcion
# se vuelve a llamar la funcion de manera recursiva
# se podria decir que este código mas facil de leer
# pero es un método menos eficiente en memoria porque agrega
# otra llamada al stack cada vez, reservando memoria
# para un nuevo contexto (variables, direcciones) cada vez

def get_int_recur():
    try:
        user_in = input("Ingrese un numero entero: ")
        my_number = int(user_in)
    except ValueError:
        print("Debe ingresar un numero entero valido!")
        return get_int_recur()
    else:
        return my_number
