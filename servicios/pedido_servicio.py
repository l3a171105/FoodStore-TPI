from entidades.pedido import Pedido
from entidades.usuario import Usuario
from entidades.producto import Producto
from enums.enums import Estado, FormaPago
from excepciones.excepciones import EntidadNoEncontradaError, OperacionNoPermitidaError

class PedidoServicio:
    def __init__(self) -> None:
        self._pedidos: list[Pedido] = []

    def listar_pedidos(self) -> list[Pedido]:
        return [ped for ped in self._pedidos if not ped.eliminado]

    def listar_pedidos_por_usuario(self, usuario: Usuario) -> list[Pedido]:
        return [ped for ped in self._pedidos if not ped.eliminado and ped.usuario.id == usuario.id]

    def buscar_por_id(self, id_pedido: int) -> Pedido:
        for ped in self._pedidos:
            if ped.id == id_pedido and not ped.eliminado:
                return ped
        raise EntidadNoEncontradaError(f"El pedido con ID {id_pedido} no existe.")

    def crear_pedido(self, usuario: Usuario, forma_pago: FormaPago, items: list[tuple[int, Producto]]) -> Pedido:
        if usuario.eliminado:
            raise OperacionNoPermitidaError("No se puede crear un pedido con un usuario eliminado[cite: 8].")
        
        nuevo_pedido = Pedido(usuario, forma_pago)
        
        try:
            for cantidad, producto in items:
                nuevo_pedido.agregar_detalle(cantidad, producto)
        except Exception as e:
            # Si ocurre un error (ej. falta de stock), se cancela la creación y no se modifica ningún stock
            raise e

        # Descontar el stock de los productos
        for detalle in nuevo_pedido.detalles:
            detalle.producto.stock -= detalle.cantidad

        self._pedidos.append(nuevo_pedido)
        return nuevo_pedido

    def actualizar_estado_y_pago(self, id_pedido: int, nuevo_estado: Estado | None = None, nueva_forma_pago: FormaPago | None = None) -> Pedido:
        pedido = self.buscar_por_id(id_pedido)

        if pedido.estado in (Estado.TERMINADO, Estado.CANCELADO):
            raise OperacionNoPermitidaError("Un pedido TERMINADO o CANCELADO no puede cambiar de estado[cite: 8].")

        if nuevo_estado:
            # Validar transiciones de estado válidas: PENDIENTE -> CONFIRMADO -> TERMINADO; PENDIENTE o CONFIRMADO -> CANCELADO
            if pedido.estado == Estado.PENDIENTE:
                if nuevo_estado not in (Estado.CONFIRMADO, Estado.CANCELADO):
                    raise OperacionNoPermitidaError("Transición de estado inválida[cite: 8].")
            elif pedido.estado == Estado.CONFIRMADO:
                if nuevo_estado not in (Estado.TERMINADO, Estado.CANCELADO):
                    raise OperacionNoPermitidaError("Transición de estado inválida[cite: 8].")

            # Si pasa a 'CANCELADO', se devuelve el stock
            if nuevo_estado == Estado.CANCELADO:
                for detalle in pedido.detalles:
                    detalle.producto.stock += detalle.cantidad

            pedido.estado = nuevo_estado

        if nueva_forma_pago:
            pedido.forma_pago = nueva_forma_pago

        return pedido

    def eliminar_pedido(self, id_pedido: int) -> None:
        pedido = self.buscar_por_id(id_pedido)
        
        # Si no estaba 'TERMINADO' ni 'CANCELADO', se devuelve el stock al eliminarlo
        if pedido.estado not in (Estado.TERMINADO, Estado.CANCELADO):
            for detalle in pedido.detalles:
                detalle.producto.stock += detalle.cantidad

        pedido.eliminado = True
        for detalle in pedido._detalles:
            detalle.eliminado = True