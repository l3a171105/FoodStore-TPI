class FoodStoreError(Exception):
    """Clase base para errores de la aplicación."""
    pass

class EntidadNoEncontradaError(FoodStoreError):
    """Se lanza cuando un id no existe o está eliminado."""
    pass

class DatoInvalidoError(FoodStoreError):
    """Se lanza ante textos vacíos o formatos incorrectos."""
    pass

class PrecioInvalidoError(DatoInvalidoError):
    """Se lanza si el precio es negativo."""
    pass

class StockInsuficienteError(FoodStoreError):
    """Se lanza cuando la cantidad pedida supera el stock disponible."""
    pass

class DuplicadoError(FoodStoreError):
    """Se lanza cuando hay un mail o nombre de categoría repetido."""
    pass

class OperacionNoPermitidaError(FoodStoreError):
    """Se lanza ante transiciones de estado inválidas o restricciones de negocio."""
    pass

class CredencialesInvalidasError(FoodStoreError):
    """Se lanza si el mail o la contraseña son incorrectos."""
    pass