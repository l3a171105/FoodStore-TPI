from __future__ import annotations
from entidades.base import Base
from entidades.producto import Producto
from excepciones.excepciones import DatoInvalidoError

class DetallePedido(Base):
    def __init__(self, cantidad: int, producto: Producto) -> None:
        super().__init__()
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = self._calcular_subtotal()

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        if valor <= 0:
            raise DatoInvalidoError("La cantidad debe ser mayor a 0.")
        self._cantidad = int(valor)
        self.subtotal = self._calcular_subtotal()

    @property
    def producto(self) -> Producto:
        return self._producto

    @producto.setter
    def producto(self, valor: Producto) -> None:
        if not isinstance(valor, Producto):
            raise DatoInvalidoError("Debe asociarse a un producto válido.")
        self._producto = valor

    @property
    def subtotal(self) -> float:
        return self._subtotal

    @subtotal.setter
    def subtotal(self, valor: float) -> None:
        self._subtotal = float(valor)

    def _calcular_subtotal(self) -> float:
        return self.cantidad * self.producto.precio

    def __str__(self) -> str:
        return f"Producto: {self.producto.nombre} | Cantidad: {self.cantidad} | Subtotal: ${self.subtotal:.2f}"