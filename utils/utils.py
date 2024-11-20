from typing import List, Optional

def solicitar_input(prompt: str, opciones: Optional[List[str]] = None) -> str:
    """Función para solicitar un input al usuario, con opciones si es necesario"""
    if opciones is None:
        opciones = []  # Si no se pasan opciones, usamos una lista vacía
    while True:
        # Solicitamos el input al usuario y lo convertimos a minúsculas
        user_input = input(prompt).lower()
        if opciones and user_input not in opciones:
            # Si el input no es válido, mostramos un mensaje con las opciones correctas
            print(f"Respuesta inválida. Las opciones son: {', '.join(opciones)}.")
        else:
            # Si el input es válido, lo retornamos
            return user_input


def verificar_ingreso(nombre: str, clientes: list):
    """Verificar si el cliente existe en la lista y devolverlo"""
    for client in clientes:
        if client.name.lower() == nombre.lower():
            # Si encontramos al cliente, lo devolvemos
            return client
    # Si no se encuentra, devolvemos None
    return None


def mostrar_menu():
    """Mostrar el menú de opciones"""
    print(colores("\n--- Menú de opciones ---", "azul"))
    print("1. Listar Clientes")
    print("2. Agregar Cliente")
    print("3. Modificar Cliente")
    print("4. Eliminar Cliente")
    print("5. Salir")

    # Solicitar al usuario que seleccione una opción del menú
    return solicitar_input("Seleccione una opción: ", ["1", "2", "3", "4", "5"])


def verificar_nombre_existente(nombre: str, clientes: list) -> bool:
    """Verificar si el cliente con ese nombre ya existe en la lista"""
    for client in clientes:
        if client.name.lower() == nombre.lower():
            # Si el cliente ya existe, retornamos True
            return True
    # Si no existe, retornamos False
    return False

def colores(texto: str, color: str = 'reset') -> str:
    """Devuelve el texto con el color deseado"""
    COLORES = {
        'rojo': '\033[31m',
        'verde': '\033[32m',
        'azul': '\033[34m',
        'negrita': '\033[1m',
        'reset': '\033[0m',  # Reset para quitar el color
    }

    # Obtenemos el código de color, por defecto 'reset' si no es válido
    color_code = COLORES.get(color.lower(), COLORES['reset'])
    # Aplicamos el color y luego restablecemos al color original
    return f"{color_code}{texto}{COLORES['reset']}"
