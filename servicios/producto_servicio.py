from entidades.producto import Producto
from entidades.categoria import Categoria
from excepciones.excepciones import EntidadNoEncontradaError, OperacionNoPermitidaError

class ProductoServicio:
    def __init__(self) -> None:
        self._productos: list[Producto] = []

    def listar_productos(self) -> list[Producto]:
        return [p for p in self._productos if not p.eliminado]

    def listar_productos_disponibles_cliente(self) -> list[Producto]:
        # Clientes ven solo productos no eliminados, disponibles y con stock
        return [p for p in self._productos if not p.eliminado and p.disponible and p.stock > 0]

    def buscar_por_id(self, id_producto: int) -> Producto:
        for p in self._productos:
            if p.id == id_producto and not p.eliminado:
                return p
        raise EntidadNoEncontradaError(f"El producto con ID {id_producto} no existe.")

    def crear_producto(self, nombre: str, precio: float, descripcion: str, stock: int, imagen: str, disponible: bool, categoria: Categoria) -> Producto:
        nuevo_producto = Producto(nombre, precio, descripcion, stock, imagen, disponible, categoria)
        self._productos.append(nuevo_producto)
        return nuevo_producto

    def editar_producto(self, id_producto: int, **kwargs) -> Producto:
        p = self.buscar_por_id(id_producto)
        if "nombre" in kwargs and kwargs["nombre"]:
            p.nombre = kwargs["nombre"]
        if "precio" in kwargs and kwargs["precio"] is not None:
            p.precio = kwargs["precio"]
        if "descripcion" in kwargs and kwargs["descripcion"]:
            p.descripcion = kwargs["descripcion"]
        if "stock" in kwargs and kwargs["stock"] is not None:
            p.stock = kwargs["stock"]
        if "imagen" in kwargs and kwargs["imagen"]:
            p.imagen = kwargs["imagen"]
        if "disponible" in kwargs and kwargs["disponible"] is not None:
            p.disponible = kwargs["disponible"]
        if "categoria" in kwargs and kwargs["categoria"]:
            p.categoria = kwargs["categoria"]
        return p

    def eliminar_producto(self, id_producto: int) -> None:
        p = self.buscar_por_id(id_producto)
        p.eliminado = True