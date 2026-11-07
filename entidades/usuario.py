from entidades.base import Base
from enums.enums import Rol
from excepciones.excepciones import DatoInvalidoError

class Usuario(Base):
    def __init__(self, nombre: str, apellido: str, mail: str, celular: str, contrasenia: str, rol: Rol) -> None:
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.celular = celular
        self.contrasenia = contrasenia
        self.rol = rol

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise DatoInvalidoError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise DatoInvalidoError("El apellido no puede estar vacío.")
        self._apellido = valor.strip()

    @property
    def mail(self) -> str:
        return self._mail

    @mail.setter
    def mail(self, valor: str) -> None:
        if not valor or "@" not in valor or "." not in valor:
            raise DatoInvalidoError("El formato del mail es inválido.")
        self._mail = valor.strip().lower()

    @property
    def celular(self) -> str:
        return self._celular

    @celular.setter
    def celular(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise DatoInvalidoError("El celular no puede estar vacío.")
        self._celular = valor.strip()

    @property
    def contrasenia(self) -> None:
        raise AttributeError("La contraseña no es accesible directamente.")

    @contrasenia.setter
    def contrasenia(self, valor: str) -> None:
        if not valor or len(valor) < 4:
            raise DatoInvalidoError("La contraseña debe tener al menos 4 caracteres.")
        self._contrasenia = valor

    def verificar_contrasenia(self, contrasenia_ingresada: str) -> bool:
        return self._contrasenia == contrasenia_ingresada

    @property
    def rol(self) -> Rol:
        return self._rol

    @rol.setter
    def rol(self, valor: Rol) -> None:
        if not isinstance(valor, Rol):
            raise DatoInvalidoError("Rol inválido.")
        self._rol = valor

    def __str__(self) -> str:
        return f"ID: {self.id} | Usuario: {self.nombre} {self.apellido} - Mail: {self.mail} - Rol: {self.rol.value}"