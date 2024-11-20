from clases import Client, PremiumClient
from utils import verificar_nombre_existente, verificar_ingreso, solicitar_input, colores

class Sistema:
    def __init__(self, clientes: list):
        # Lista de clientes en el sistema
        self.clientes = clientes

    def agregar_cliente(self):
        """Agregar un nuevo cliente al sistema"""
        nombre = self.solicitar_dato("Ingrese el nombre del nuevo cliente: ")
        # Verificamos si el cliente ya existe
        if verificar_nombre_existente(nombre, self.clientes):
            print(colores("El cliente ya existe.", "rojo"))
            return
        
        # Solicitar el resto de los datos
        mail = self.solicitar_dato("Ingrese el correo del cliente: ")
        telefono = self.solicitar_dato("Ingrese el teléfono del cliente: ")
        direccion = self.solicitar_dato("Ingrese la dirección del cliente: ")

        # Preguntamos si es premium
        es_premium = solicitar_input("¿El cliente es premium? (s/n): ", ["s", "n"]) == "s"
        if es_premium:
            nuevo_cliente = PremiumClient(nombre, mail, telefono, direccion, es_premium)
        else:
            nuevo_cliente = Client(nombre, mail, telefono, direccion)
        
        # Agregamos el cliente a la lista
        self.clientes.append(nuevo_cliente)
        print(colores(f"Cliente {nombre} agregado exitosamente.", "verde"))

    def solicitar_dato(self, mensaje):
        """Solicitar un dato al usuario y validar que no esté vacío"""
        dato = input(mensaje).strip()
        while not dato:
            # Si el dato está vacío, pedimos nuevamente la entrada
            print(colores("Este campo no puede estar vacío. Inténtelo nuevamente.", "rojo"))
            dato = input(mensaje).strip()
        return dato

    def modificar_cliente(self):
        """Modificar los atributos de un cliente existente"""
        nombre = input("Ingrese el nombre del cliente a modificar: ")
        cliente = verificar_ingreso(nombre, self.clientes)

        if not cliente:
            # Si el cliente no existe, mostramos un mensaje de error
            print(colores("Cliente no encontrado.", "rojo"))
            return
        
        # Preguntamos qué atributo se desea modificar
        print(f"¿Qué atributo desea modificar para el cliente {cliente.name}?")
        print("1. Nombre")
        print("2. Dirección")
        print("3. Teléfono")
        if isinstance(cliente, PremiumClient):
            print("4. Estatus Premium")
        
        # Obtenemos la opción seleccionada
        atributo = solicitar_input("Seleccione una opción: ", ["1", "2", "3", "4"] if isinstance(cliente, PremiumClient) else ["1", "2", "3"])

        # Modificamos el atributo según la opción seleccionada
        if atributo == "1":
            nuevo_nombre = self.solicitar_dato("Ingrese el nuevo nombre: ")
            cliente.name = nuevo_nombre
        elif atributo == "2":
            nueva_direccion = input("Ingrese la nueva dirección: ")
            cliente.update_address(nueva_direccion)
        elif atributo == "3":
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            cliente.update_phone(nuevo_telefono)
        elif atributo == "4" and isinstance(cliente, PremiumClient):
            nuevo_estado = solicitar_input("¿Cambiar a cliente premium? (s/n): ", ["s", "n"]) == "s"
            cliente.update_premium_status(nuevo_estado)
        else:
            # Si la opción no es válida, mostramos un error
            print(colores("Opción no válida.", "rojo"))

    def listar_clientes(self):
        """Listar todos los clientes en el sistema"""
        if not self.clientes:
            # Si no hay clientes, mostramos un mensaje
            print(colores("No hay clientes registrados.", "rojo"))
            return
        # Si hay clientes, mostramos la lista
        print(colores("\nListado de Clientes: \n", "azul"))
        for cliente in self.clientes:
            print(f"{cliente}\n")
    
    def eliminar_cliente(self):
        """Eliminar un cliente del sistema"""
        nombre = input("Ingrese el nombre del cliente a eliminar: ")
        cliente = verificar_ingreso(nombre, self.clientes)

        if not cliente:
            # Si el cliente no existe, mostramos un mensaje de error
            print(colores("Cliente no encontrado.", "rojo"))
            return

        # Confirmación antes de eliminar
        confirmacion = solicitar_input(
            f"¿Está seguro de que desea eliminar al cliente '{nombre}'? (s/n): ", ["s", "n"]
        )
        if confirmacion == "s":
            # Si la respuesta es afirmativa, eliminamos al cliente
            self.clientes.remove(cliente)
            print(colores(f"El cliente '{nombre}' ha sido eliminado exitosamente.", "verde"))
        else:
            # Si la respuesta es negativa, cancelamos la operación
            print("Operación cancelada.")
