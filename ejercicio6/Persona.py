class Persona:
    def __init__(self, name: str = '', age: int = 0, dni: int = 0):
        self.set_name(name)
        self.set_age(age)
        self.set_dni(dni)

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres.")
    
    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int):
        if isinstance(age, int) and age >= 0:
            self._age = age
        else:
            raise ValueError("La edad debe ser un número entero no negativo.")
    
    def get_dni(self) -> int:
        return self._dni
    
    def set_dni(self, dni: int):
        if isinstance(dni, int) and dni >= 0:
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser un número entero no negativo.")
    
    def mostrar(self):
        print("=== Persona ===")
        print(f"Nombre: {self._name}")
        print(f"Edad: {self._age}")
        print(f"DNI: {self._dni}")

    def es_mayor_de_edad(self) -> bool:
        return self._age >= 18