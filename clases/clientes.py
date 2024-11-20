from utils import colores

class Client:
    def __init__(self, name: str, mail: str, phone: str, address: str) -> None:
        # Inicializamos los datos del cliente
        self.name = name  # Nombre del cliente
        self.mail = mail  # Correo electrónico Aca es email.
        self.phone = phone  # Teléfono
        self.address = address  # Dirección

    def update_address(self, new_address: str) -> None:
        """Actualizar la dirección del cliente"""
        self.address = new_address
        print(colores(f"La dirección del cliente {self.name} se actualizó a: {self.address}.", "verde"))

    def update_phone(self, new_phone: str) -> None:
        """Actualizar el teléfono del cliente"""
        self.phone = new_phone
        print(f"El teléfono del cliente {self.name} se actualizó a: {self.phone}.")

    def __str__(self): # El metodo str tiene que ser sencillo y corto, mostrando un dato unico
        # Por ejemplo return f"Cliente: {self.mail}"
        """Representación en forma de cadena de texto del cliente"""
        return "\n".join([
            f"{colores('NOMBRE', 'negrita')}: {colores(self.name, 'verde')}",
            f"{colores('EMAIL', 'negrita')}: {self.mail}",
            f"{colores('DIRECCION', 'negrita')}: {self.address}",
            f"{colores('TELEFONO', 'negrita')}: {self.phone}"
        ]) # Y este metodo movelo a uno como def mostrar_datos(self):


class PremiumClient(Client):
    def __init__(self, name: str, mail: str, phone: str, address: str, premium_status: bool) -> None:
        # Usamos el constructor de la clase base (Client)
        super().__init__(name, mail, phone, address)
        self.premium_status = premium_status  # Estado de cliente premium

    def update_premium_status(self, new_status: bool) -> None:
        """Actualizar el estado de cliente premium"""
        self.premium_status = new_status
        status = "premium" if self.premium_status else "no premium"
        print(colores(f"El estatus del cliente {self.name} es ahora: {status}.", "verde"))

    @staticmethod
    def validar_respuesta_premium():
        """Validar si el cliente es premium"""
        respuesta = input("¿Es cliente premium? (si/no): ").lower()
        return respuesta == "si"

    def __str__(self):
        """Mostrar la información completa del cliente premium"""
        return super().__str__() + colores(f"\nESTATUS: {'Premium' if self.premium_status else 'No Premium'}", "azul")
