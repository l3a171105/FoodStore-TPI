from entidades.base import Base
from excepciones.excepciones import DatoInvalidoError

class Categoria(Base):
    def __init__(self, nombre: str, descripcion: str) -> None:
        super().__init__()
        self.nombre = nombre
        self.descripcion = descripcion

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise DatoInvalidoError("El nombre de la categoría no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise DatoInvalidoError("La descripción de la categoría no puede estar vacía.")
        self._descripcion = valor.strip()

    def __str__(self) -> str:
        return f"ID: {self.id} | Categoría: {self.nombre} - Descripción: {self.descripcion}"