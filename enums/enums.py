from enum import Enum

class Rol(Enum):
    ADMIN = "ADMIN"
    USUARIO = "USUARIO"

class Estado(Enum):
    PENDIENTE = "PENDIENTE"
    CONFIRMADO = "CONFIRMADO"
    TERMINADO = "TERMINADO"
    CANCELADO = "CANCELADO"

class FormaPago(Enum):
    TARJETA = "TARJETA"
    TRANSFERENCIA = "TRANSFERENCIA"
    EFECTIVO = "EFECTIVO"