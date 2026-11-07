from abc import ABC, abstractmethod
from datetime import datetime

class Calculable(ABC):
    @abstractmethod
    def calcular_total(self) -> None:
        """Actualiza el total del objeto que la implementa."""
        pass

class Base(ABC):
    _contador_id: int = 1  # Contador de clase para los IDs

    def __init__(self) -> None:
        self._id: int = Base._contador_id
        Base._contador_id += 1
        self._eliminado: bool = False
        self._creado_en: datetime = datetime.now()

    @property
    def id(self) -> int:
        return self._id

    @property
    def eliminado(self) -> bool:
        return self._eliminado

    @eliminado.setter
    def eliminado(self, valor: bool) -> None:
        self._eliminado = valor

    @property
    def creado_en(self) -> datetime:
        return self._creado_en

    def __eq__(self, otro: object) -> bool:
        if isinstance(otro, Base):
            return self._id == otro._id
        return False