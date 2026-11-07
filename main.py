from servicios.categoria_servicio import CategoriaServicio
from servicios.producto_servicio import ProductoServicio
from servicios.usuario_servicio import UsuarioServicio
from servicios.pedido_servicio import PedidoServicio
from enums.enums import Rol
from excepciones.excepciones import FoodStoreError, CredencialesInvalidasError
from consola.menu import crear_menu

def main() -> None:
    cat_serv = CategoriaServicio()
    prod_serv = ProductoServicio()
    user_serv = UsuarioServicio()
    ped_serv = PedidoServicio()

    # Cargar administrador inicial obligatorio
    user_serv.crear_usuario("Ana", "Pérez", "admin@foodstore.com", "1122334455", "admin123", Rol.ADMIN)
    # Cargar un cliente de prueba opcional
    user_serv.crear_usuario("Juan", "Gómez", "juan@foodstore.com", "1199887766", "juan123", Rol.USUARIO)

    print("=== BIENVENIDO A FOOD STORE ===")

    while True:
        intentos = 3
        usuario_actual = None

        while intentos > 0:
            print(f"\n--- INICIO DE SESIÓN (Intentos restantes: {intentos}) ---")
            mail = input("Mail: ").strip()
            contrasenia = input("Contraseña: ").strip()

            try:
                usuario_actual = user_serv.autenticar(mail, contrasenia)
                print(f"¡Bienvenido/a, {usuario_actual.nombre} {usuario_actual.apellido} [{usuario_actual.rol.value}]!")
                break
            except CredencialesInvalidasError:
                intentos -= 1
                print("Mail o contraseña incorrectos.")  # Mismo mensaje para no revelar fallos
            except FoodStoreError as e:
                intentos -= 1
                print(f"Error: {e}")

        if not usuario_actual:
            print("\nSe han agotado los 3 intentos. El programa ha finalizado.")
            break

        # Crear y mostrar el menú usando polimorfismo
        menu = crear_menu(usuario_actual, cat_serv, prod_serv, user_serv, ped_serv)
        cerrar_sesion = menu.mostrar()

        if not cerrar_sesion:
            print("\n¡Gracias por usar Food Store!")
            break

if __name__ == "__main__":
    main()