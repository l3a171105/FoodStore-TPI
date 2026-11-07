from abc import ABC, abstractmethod
from entidades.usuario import Usuario
from enums.enums import Rol, Estado, FormaPago
from servicios.categoria_servicio import CategoriaServicio
from servicios.producto_servicio import ProductoServicio
from servicios.usuario_servicio import UsuarioServicio
from servicios.pedido_servicio import PedidoServicio
from excepciones.excepciones import FoodStoreError

class Menu(ABC):
    def __init__(self, usuario: Usuario, cat_serv: CategoriaServicio, prod_serv: ProductoServicio, user_serv: UsuarioServicio, ped_serv: PedidoServicio) -> None:
        self._usuario = usuario
        self._cat_serv = cat_serv
        self._prod_serv = prod_serv
        self._user_serv = user_serv
        self._ped_serv = ped_serv

    @abstractmethod
    def mostrar(self) -> bool:
        """True = cerrar sesión, False = salir del programa[cite: 6]."""
        pass


class MenuAdministrador(Menu):
    def mostrar(self) -> bool:
        while True:
            print(f"\n=== FOOD STORE ADMINISTRADOR ({self._usuario.nombre} {self._usuario.apellido}) ===")
            print("1. Categorías")
            print("2. Productos")
            print("3. Usuarios")
            print("4. Pedidos")
            print("9. Cerrar sesión")
            print("0. Salir")
            
            opcion = input("Seleccione: ").strip()
            
            try:
                if opcion == "1":
                    self._menu_categorias()
                elif opcion == "2":
                    self._menu_productos()
                elif opcion == "3":
                    self._menu_usuarios()
                elif opcion == "4":
                    self._menu_pedidos()
                elif opcion == "9":
                    return True  # Cerrar sesión
                elif opcion == "0":
                    return False  # Salir
                else:
                    print("Opción inválida. Intente nuevamente.")
            except FoodStoreError as e:
                print(f"[ERROR DE NEGOCIO]: {e}")
            except ValueError:
                print("[ERROR]: Entrada numérica inválida.")

    def _menu_categorias(self) -> None:
        while True:
            print("\n--- GESTIÓN DE CATEGORÍAS ---")
            print("1. Listar")
            print("2. Crear")
            print("3. Editar")
            print("4. Eliminar")
            print("0. Volver")
            op = input("Seleccione: ").strip()
            
            if op == "1":
                cats = self._cat_serv.listar_categorias()
                if not cats:
                    print("No hay categorías cargadas.")
                for c in cats:
                    print(c)
            elif op == "2":
                nombre = input("Nombre de la categoría: ")
                desc = input("Descripción: ")
                c = self._cat_serv.crear_categoria(nombre, desc)
                print(f"¡Categoría creada con éxito! ID generado: {c.id}")
            elif op == "3":
                cats = self._cat_serv.listar_categorias()
                for c in cats: print(c)
                id_cat = int(input("Ingrese el ID de la categoría a editar: "))
                nuevo_nombre = input("Nuevo nombre (dejar vacío para conservar): ")
                nueva_desc = input("Nueva descripción (dejar vacío para conservar): ")
                self._cat_serv.editar_categoria(id_cat, nuevo_nombre if nuevo_nombre else None, nueva_desc if nueva_desc else None)
                print("¡Categoría actualizada con éxito!")
            elif op == "4":
                cats = self._cat_serv.listar_categorias()
                for c in cats: print(c)
                id_cat = int(input("Ingrese el ID de la categoría a eliminar: "))
                confirmar = input("¿Confirma la baja lógica? (S/N): ").strip().upper()
                if confirmar == 'S':
                    self._cat_serv.eliminar_categoria(id_cat)
                    print("¡Categoría eliminada con éxito!")
            elif op == "0":
                break
            else:
                print("Opción inválida.")

    def _menu_productos(self) -> None:
        while True:
            print("\n--- GESTIÓN DE PRODUCTOS ---")
            print("1. Listar")
            print("2. Crear")
            print("3. Editar")
            print("4. Eliminar")
            print("0. Volver")
            op = input("Seleccione: ").strip()
            
            if op == "1":
                prods = self._prod_serv.listar_productos()
                if not prods:
                    print("No hay productos cargados.")
                for p in prods:
                    print(p)
            elif op == "2":
                cats = self._cat_serv.listar_categorias()
                for c in cats: print(c)
                id_cat = int(input("ID de la categoría asociada: "))
                cat = self._cat_serv.buscar_por_id(id_cat)
                
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                desc = input("Descripción: ")
                stock = int(input("Stock inicial: "))
                imagen = input("URL o ruta de imagen: ")
                disp_input = input("¿Está disponible? (S/N): ").strip().upper()
                disponible = True if disp_input == 'S' else False
                
                p = self._prod_serv.crear_producto(nombre, precio, desc, stock, imagen, disponible, cat)
                print(f"¡Producto creado con éxito! ID generado: {p.id}")
            elif op == "3":
                prods = self._prod_serv.listar_productos()
                for p in prods: print(p)
                id_prod = int(input("Ingrese el ID del producto a editar: "))
                
                nombre = input("Nuevo nombre (Enter para conservar): ")
                precio_str = input("Nuevo precio (Enter para conservar): ")
                desc = input("Nueva descripción (Enter para conservar): ")
                stock_str = input("Nuevo stock (Enter para conservar): ")
                imagen = input("Nueva imagen (Enter para conservar): ")
                disp_str = input("¿Disponible? (S/N, Enter para conservar): ").strip().upper()
                
                kwargs = {}
                if nombre: kwargs["nombre"] = nombre
                if precio_str: kwargs["precio"] = float(precio_str)
                if desc: kwargs["descripcion"] = desc
                if stock_str: kwargs["stock"] = int(stock_str)
                if imagen: kwargs["imagen"] = imagen
                if disp_str: kwargs["disponible"] = True if disp_str == 'S' else False
                
                self._prod_serv.editar_producto(id_prod, **kwargs)
                print("¡Producto actualizado con éxito!")
            elif op == "4":
                prods = self._prod_serv.listar_productos()
                for p in prods: print(p)
                id_prod = int(input("Ingrese el ID del producto a eliminar: "))
                if input("¿Confirma baja lógica? (S/N): ").strip().upper() == 'S':
                    self._prod_serv.eliminar_producto(id_prod)
                    print("¡Producto eliminado con éxito!")
            elif op == "0":
                break
            else:
                print("Opción inválida.")

    def _menu_usuarios(self) -> None:
        while True:
            print("\n--- GESTIÓN DE USUARIOS ---")
            print("1. Listar")
            print("2. Crear")
            print("3. Eliminar")
            print("0. Volver")
            op = input("Seleccione: ").strip()
            
            if op == "1":
                users = self._user_serv.listar_usuarios()
                for u in users: print(u)
            elif op == "2":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                mail = input("Mail: ")
                celular = input("Celular: ")
                contrasenia = input("Contraseña: ")
                print("Rol: 1. ADMIN | 2. USUARIO")
                rol_op = input("Seleccione rol: ").strip()
                rol = Rol.ADMIN if rol_op == "1" else Rol.USUARIO
                
                u = self._user_serv.crear_usuario(nombre, apellido, mail, celular, contrasenia, rol)
                print(f"¡Usuario creado con éxito! ID generado: {u.id}")
            elif op == "3":
                users = self._user_serv.listar_usuarios()
                for u in users: print(u)
                id_u = int(input("Ingrese el ID del usuario a eliminar: "))
                if input("¿Confirma baja lógica? (S/N): ").strip().upper() == 'S':
                    self._user_serv.eliminar_usuario(id_u, self._usuario.id)
                    print("¡Usuario eliminado con éxito!")
            elif op == "0":
                break
            else:
                print("Opción inválida.")

    def _menu_pedidos(self) -> None:
        while True:
            print("\n--- GESTIÓN DE PEDIDOS ---")
            print("1. Listar pedidos")
            print("2. Crear pedido")
            print("3. Cambiar estado / forma de pago")
            print("4. Eliminar pedido")
            print("0. Volver")
            op = input("Seleccione: ").strip()
            
            if op == "1":
                peds = self._ped_serv.listar_pedidos()
                if not peds:
                    print("No hay pedidos registrados.")
                for ped in peds:
                    print(ped)
                    for det in ped.detalles:
                        print(f"   -> {det}")
            elif op == "2":
                users = self._user_serv.listar_usuarios()
                for u in users: print(u)
                id_u = int(input("ID del usuario para el pedido: "))
                usuario = self._user_serv.buscar_por_id(id_u)
                
                print("Forma de pago: 1. TARJETA | 2. TRANSFERENCIA | 3. EFECTIVO")
                fp_op = input("Seleccione forma de pago: ").strip()
                forma_pago = FormaPago.TARJETA if fp_op == "1" else (FormaPago.TRANSFERENCIA if fp_op == "2" else FormaPago.EFECTIVO)
                
                items = []
                while True:
                    prods = self._prod_serv.listar_productos_disponibles_cliente()
                    for p in prods: print(p)
                    id_p = int(input("ID del producto a agregar (0 para terminar): "))
                    if id_p == 0:
                        break
                    prod = self._prod_serv.buscar_por_id(id_p)
                    cant = int(input(f"Cantidad (Stock disponible: {prod.stock}): "))
                    items.append((cant, prod))
                
                if items:
                    nuevo_ped = self._ped_serv.crear_pedido(usuario, forma_pago, items)
                    print(f"¡Pedido creado con éxito! ID: {nuevo_ped.id} | Total: ${nuevo_ped.total:.2f}")
                else:
                    print("No se agregaron ítems, pedido cancelado.")
            elif op == "3":
                peds = self._ped_serv.listar_pedidos()
                for ped in peds: print(ped)
                id_ped = int(input("ID del pedido a modificar: "))
                
                print("Nuevo estado: 1. CONFIRMADO | 2. TERMINADO | 3. CANCELADO | (Enter para no cambiar)")
                est_op = input("Seleccione estado: ").strip()
                nuevo_estado = None
                if est_op == "1": nuevo_estado = Estado.CONFIRMADO
                elif est_op == "2": nuevo_estado = Estado.TERMINADO
                elif est_op == "3": nuevo_estado = Estado.CANCELADO
                
                print("Nueva forma de pago: 1. TARJETA | 2. TRANSFERENCIA | 3. EFECTIVO | (Enter para no cambiar)")
                fp_op = input("Seleccione pago: ").strip()
                nueva_fp = None
                if fp_op == "1": nueva_fp = FormaPago.TARJETA
                elif fp_op == "2": nueva_fp = FormaPago.TRANSFERENCIA
                elif fp_op == "3": nueva_fp = FormaPago.EFECTIVO
                
                self._ped_serv.actualizar_estado_y_pago(id_ped, nuevo_estado, nueva_fp)
                print("¡Pedido actualizado con éxito!")
            elif op == "4":
                peds = self._ped_serv.listar_pedidos()
                for ped in peds: print(ped)
                id_ped = int(input("ID del pedido a eliminar: "))
                if input("¿Confirma baja lógica? (S/N): ").strip().upper() == 'S':
                    self._ped_serv.eliminar_pedido(id_ped)
                    print("¡Pedido eliminado con éxito!")
            elif op == "0":
                break
            else:
                print("Opción inválida.")


class MenuCliente(Menu):
    def mostrar(self) -> bool:
        while True:
            print(f"\n=== FOOD STORE CLIENTE ({self._usuario.nombre} {self._usuario.apellido}) ===")
            print("1. Ver categorías")
            print("2. Ver productos disponibles")
            print("3. Mis pedidos")
            print("4. Mis datos")
            print("9. Cerrar sesión")
            print("0. Salir")
            
            opcion = input("Seleccione: ").strip()
            
            try:
                if opcion == "1":
                    for c in self._cat_serv.listar_categorias():
                        print(c)
                elif opcion == "2":
                    for p in self._prod_serv.listar_productos_disponibles_cliente():
                        print(p)
                elif opcion == "3":
                    peds = self._ped_serv.listar_pedidos_por_usuario(self._usuario)
                    if not peds:
                        print("No tienes pedidos registrados.")
                    for ped in peds:
                        print(ped)
                        for det in ped.detalles:
                            print(f"   -> {det}")
                elif opcion == "4":
                    print(self._usuario)
                elif opcion == "9":
                    return True
                elif opcion == "0":
                    return False
                else:
                    print("Opción inválida.")
            except FoodStoreError as e:
                print(f"[ERROR DE NEGOCIO]: {e}")
            except ValueError:
                print("[ERROR]: Entrada numérica inválida.")


def crear_menu(usuario: Usuario, cat_serv: CategoriaServicio, prod_serv: ProductoServicio, user_serv: UsuarioServicio, ped_serv: PedidoServicio) -> Menu:
    if usuario.rol == Rol.ADMIN:
        return MenuAdministrador(usuario, cat_serv, prod_serv, user_serv, ped_serv)
    return MenuCliente(usuario, cat_serv, prod_serv, user_serv, ped_serv)