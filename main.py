from utils import mostrar_menu, colores
from clases import Sistema, Client, PremiumClient

# Lista de clientes (comenzamos con algunos clientes de ejemplo)
clientes = [
    Client("Nico", "tutor_restrella@ejemplo.com", "+5491164265987", "Calle falsa 123"),
    PremiumClient("Federico", "meduele@elcerebro.net", "+54112354568", "Elm Street 666", True),
    Client("Ana", "ana.lopez@example.com", "+5491122334455", "Av. Corrientes 1234"),
    PremiumClient("Luis", "luis.gonzalez@premium.com", "+541134567890", "Calle San Martín 4321", True),
    Client("María", "maria.rodriguez@example.com", "+5491167890123", "Avenida Libertador 5678")
]

# Creamos una instancia del sistema con la lista de clientes
sistema = Sistema(clientes)

def main():
    """Función principal que ejecuta el menú del sistema"""
    while True:
        # Mostramos el menú y obtenemos la opción del usuario
        opcion = mostrar_menu()

        # Verificamos la opción seleccionada por el usuario
        if opcion == "1":
            sistema.listar_clientes()  # Listar todos los clientes
        elif opcion == "2":
            sistema.agregar_cliente()  # Agregar un nuevo cliente
        elif opcion == "3":
            sistema.modificar_cliente()  # Modificar un cliente existente
        elif opcion == "4":
            sistema.eliminar_cliente()  # Eliminar un cliente
        elif opcion == "5":
            # Despedimos al usuario con un mensaje de salida
            print(f"{colores('¡Hasta luego!', 'verde')}")
            texto = """
                Gracias por utilizar mi programa.
                Atte. Federico Furgiuele
            """
            print(f"{colores(texto, 'azul')}")

            break  # Terminamos el ciclo y salimos del programa

# Solo ejecutamos el main si este archivo es el principal
if __name__ == "__main__":
    main()
