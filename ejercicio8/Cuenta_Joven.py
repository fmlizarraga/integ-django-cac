from ejercicio6.Persona import Persona
from ejercicio7.Cuenta import Cuenta

class Cuenta_Joven(Cuenta):
    def __init__(self, titular: Persona, cantidad: float = 0.0, bonif: float = 0.0):
        super().__init__(titular, cantidad)
        self.set_bonif(bonif)

    def get_bonif(self) -> float:
        return self._bonif
    
    def set_bonif(self, valor: float):
        if isinstance(valor, (int, float)) and 0 <= valor <= 100:
            self._bonif = valor
        else:
            raise ValueError("El valor para la bonificación debe ser un número entre 0 y 100 (%)")
    
    def es_titular_valido(self) -> bool:
        return self._titular.es_mayor_de_edad and self._titular.get_age() < 25
    
    def retirar(self, valor: float):
        if self.es_titular_valido():
            super().retirar(valor)
        else:
            print("Retiro no permitido: El titular no es válido para una Cuenta Joven.")
    
    def mostrar(self):
        print("\n==== Cuenta Joven ====")
        print(f"Bonificación: {self.get_bonif()}%")
        return super().mostrar()