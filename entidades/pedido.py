from __future__ import annotations
from datetime import date
from entidades.base import Base
from entidades.base import Calculable
from entidades.usuario import Usuario
from entidades.producto import Producto
from entidades.detalle_pedido import DetallePedido
from enums.enums import Estado, FormaPago
from excepciones.excepciones import DatoInvalidoError, StockInsuficienteError, EntidadNoEncontradaError

class Pedido(Base, Calculable):
    def __init__(self, usuario: Usuario, forma_pago: FormaPago) -> None:
        super().__init__()
        self.usuario = usuario
        self.fecha = date.today()
        self.estado = Estado.PENDIENTE
        self.forma_pago = forma_pago
        self._detalles: list[DetallePedido] = []
        self._total: float = 0.0

    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @usuario.setter
    def usuario(self, valor: Usuario) -> None:
        if not isinstance(valor, Usuario) or valor.eliminado:
            raise DatoInvalidoError("El pedido debe estar asociado a un usuario válido y activo.")
        self._usuario = valor

    @property
    def fecha(self) -> date:
        return self._fecha

    @fecha.setter
    def fecha(self, valor: date) -> None:
        self._fecha = valor

    @property
    def estado(self) -> Estado:
        return self._estado

    @estado.setter
    def estado(self, valor: Estado) -> None:
        if not isinstance(valor, Estado):
            raise DatoInvalidoError("Estado de pedido inválido.")
        self._estado = valor

    @property
    def forma_pago(self) -> FormaPago:
        return self._forma_pago

    @forma_pago.setter
    def forma_pago(self, valor: FormaPago) -> None:
        if not isinstance(valor, FormaPago):
            raise DatoInvalidoError("Forma de pago inválida.")
        self._forma_pago = valor

    @property
    def total(self) -> float:
        return self._total

    @property
    def detalles(self) -> tuple[DetallePedido, ...]:
        # Devuelve una tupla para proteger la lista interna
        return tuple(self._detalles)

    def agregar_detalle(self, cantidad: int, producto: Producto) -> None:
        if cantidad <= 0:
            raise DatoInvalidoError("La cantidad debe ser mayor a 0.")
        if not producto.disponible or producto.stock < cantidad:
            raise StockInsuficienteError(f"Stock insuficiente para el producto: {producto.nombre}")

        # Verificar si ya existe el producto en el pedido para sumar la cantidad
        detalle_existente = self.buscar_detalle_por_producto(producto)
        if detalle_existente:
            nueva_cantidad = detalle_existente.cantidad + cantidad
            if producto.stock < nueva_cantidad:
                raise StockInsuficienteError(f"Stock insuficiente para acumular {nueva_cantidad} unidades.")
            detalle_existente.cantidad = nueva_cantidad
        else:
            nuevo_detalle = DetallePedido(cantidad, producto)
            self._detalles.append(nuevo_detalle)

        self.calcular_total()

    def buscar_detalle_por_producto(self, producto: Producto) -> DetallePedido | None:
        for detalle in self._detalles:
            if detalle.producto.id == producto.id:
                return detalle
        return None

    def eliminar_detalle_por_producto(self, producto: Producto) -> None:
        detalle = self.buscar_detalle_por_producto(producto)
        if not detalle:
            raise EntidadNoEncontradaError("El producto no se encuentra en los detalles del pedido.")
        self._detalles.remove(detalle)
        self.calcular_total()

    def calcular_total(self) -> None:
        self._total = sum(detalle.subtotal for detalle in self._detalles)

    def __str__(self) -> str:
        return (f"ID Pedido: {self.id} | Usuario: {self.usuario.nombre} {self.usuario.apellido} | "
                f"Fecha: {self.fecha} | Estado: {self.estado.value} | Pago: {self.forma_pago.value} | Total: ${self.total:.2f}")