from ejercicio6.Persona import Persona

class Cuenta:
    def __init__(self, titular: Persona, cantidad: float = 0.00):
        self._titular = titular
        self._cantidad = cantidad

    def get_titular(self) -> Persona:
        return self._titular
    
    def set_titular(self, titular: Persona):
        self._titular = titular
    
    def get_cantidad(self) -> float:
        return self._cantidad
    
    def mostrar(self):
        print("=== Cuenta ===")
        self._titular.mostrar()
        print("=== Detalle ===")
        print(f"Cantidad: {self._cantidad:.2f}")
    
    def ingresar(self, valor: float):
        if isinstance(valor, (int, float)) and valor > 0:
            self._cantidad += valor
        else:
            print("El valor debe ser un número positivo.")
    
    def retirar(self, valor: float):
        if isinstance(valor, (int, float)) and valor > 0:
            self._cantidad -= valor
        else:
            print("El valor debe ser un número positivo.")
