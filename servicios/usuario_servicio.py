from entidades.usuario import Usuario
from enums.enums import Rol
from excepciones.excepciones import EntidadNoEncontradaError, DuplicadoError, CredencialesInvalidasError, OperacionNoPermitidaError

class UsuarioServicio:
    def __init__(self) -> None:
        self._usuarios: list[Usuario] = []

    def listar_usuarios(self) -> list[Usuario]:
        return [u for u in self._usuarios if not u.eliminado]

    def buscar_por_id(self, id_usuario: int) -> Usuario:
        for u in self._usuarios:
            if u.id == id_usuario and not u.eliminado:
                return u
        raise EntidadNoEncontradaError(f"El usuario con ID {id_usuario} no existe.")

    def crear_usuario(self, nombre: str, apellido: str, mail: str, celular: str, contrasenia: str, rol: Rol) -> Usuario:
        # Validar mail único[cite: 8, 13]
        for u in self._usuarios:
            if u.mail.lower() == mail.lower():
                raise DuplicadoError("El mail ingresado ya se encuentra registrado.")
        
        nuevo_usuario = Usuario(nombre, apellido, mail, celular, contrasenia, rol)
        self._usuarios.append(nuevo_usuario)
        return nuevo_usuario

    def autenticar(self, mail: str, contrasenia: str) -> Usuario:
        for u in self._usuarios:
            if u.mail.lower() == mail.lower() and not u.eliminado:
                if u.verificar_contrasenia(contrasenia):
                    return u
        # El mensaje es el mismo para no revelar qué dato falló[cite: 5]
        raise CredencialesInvalidasError("Mail o contraseña incorrectos[cite: 5].")

    def eliminar_usuario(self, id_usuario: int, usuario_sesion_id: int) -> None:
        u = self.buscar_por_id(id_usuario)
        if u.id == usuario_sesion_id:
            raise OperacionNoPermitidaError("Un administrador no puede eliminarse a sí mismo mientras tiene la sesión iniciada[cite: 8, 13].")
        u.eliminado = True