from entidades.categoria import Categoria
from excepciones.excepciones import EntidadNoEncontradaError, DuplicadoError, OperacionNoPermitidaError

class CategoriaServicio:
    def __init__(self) -> None:
        self._categorias: list[Categoria] = []

    def listar_categorias(self) -> list[Categoria]:
        return [c for c in self._categorias if not c.eliminado]

    def buscar_por_id(self, id_categoria: int) -> Categoria:
        for cat in self._categorias:
            if cat.id == id_categoria and not cat.eliminado:
                return cat
        raise EntidadNoEncontradaError(f"La categoría con ID {id_categoria} no existe.")

    def crear_categoria(self, nombre: str, descripcion: str) -> Categoria:
        # Validar nombre único (sin distinguir mayúsculas)
        for cat in self._categorias:
            if not cat.eliminado and cat.nombre.lower() == nombre.lower():
                raise DuplicadoError(f"Ya existe una categoría con el nombre '{nombre}'.")
        
        nueva_categoria = Categoria(nombre, descripcion)
        self._categorias.append(nueva_categoria)
        return nueva_categoria

    def editar_categoria(self, id_categoria: int, nuevo_nombre: str | None = None, nueva_descripcion: str | None = None) -> Categoria:
        cat = self.buscar_por_id(id_categoria)
        
        if nuevo_nombre and nuevo_nombre.strip():
            for c in self._categorias:
                if not c.eliminado and c.id != id_categoria and c.nombre.lower() == nuevo_nombre.lower():
                    raise DuplicadoError(f"Ya existe otra categoría con el nombre '{nuevo_nombre}'.")
            cat.nombre = nuevo_nombre
            
        if nueva_descripcion and nueva_descripcion.strip():
            cat.descripcion = nueva_descripcion
            
        return cat

    def eliminar_categoria(self, id_categoria: int, productos_activos_ids: list[int] = []) -> None:
        cat = self.buscar_por_id(id_categoria)
        if productos_activos_ids:
            raise OperacionNoPermitidaError("No se puede eliminar una categoría con productos activos[cite: 8, 12].")
        cat.eliminado = True