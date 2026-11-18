# Food Store

Sistema de gestión de productos, categorías, usuarios y pedidos desarrollado en Python como Trabajo Práctico Integrador de la materia **Programación II**.

## Descripción

Food Store es una aplicación de consola que permite administrar las operaciones principales de un negocio de comidas. El sistema cuenta con diferentes funcionalidades según el tipo de usuario que inicia sesión, diferenciando entre administrador y cliente.

El proyecto fue desarrollado aplicando conceptos de Programación Orientada a Objetos (POO), buscando mantener una estructura modular, organizada y fácil de mantener.

## Funcionalidades principales

- **Inicio de sesión:** autenticación de usuarios mediante correo electrónico y contraseña.
- **Gestión de categorías:** administración de las categorías de productos.
- **Gestión de productos:** creación, consulta y modificación de productos, incluyendo sus precios y stock.
- **Gestión de usuarios:** administración de las cuentas y sus respectivos roles.
- **Gestión de pedidos:** creación, consulta y cancelación de pedidos.
- **Control de stock:** validación de las cantidades disponibles al realizar pedidos.
- **Roles de usuario:** acceso a diferentes opciones según se ingrese como administrador o cliente.
- **Manejo de excepciones:** control de errores y validaciones para evitar operaciones incorrectas.

## Tecnologías y conceptos utilizados

- Python 3.
- Programación Orientada a Objetos.
- Clases y objetos.
- Encapsulamiento.
- Herencia.
- Polimorfismo.
- Enumeraciones (`Enum`).
- Clases abstractas (`ABC`).
- Propiedades (`@property`).
- Excepciones personalizadas.
- Anotaciones de tipos (*Type Hints*).

## Estructura del proyecto

```text
FoodStore-TPI/
│
├── consola/
│   └── menu.py
│
├── entidades/
│   ├── base.py
│   ├── categoria.py
│   ├── detalle_pedido.py
│   ├── pedido.py
│   ├── producto.py
│   └── usuario.py
│
├── enums/
│   └── enums.py
│
├── excepciones/
│   └── excepciones.py
│
├── servicios/
│   ├── categoria_servicio.py
│   ├── pedido_servicio.py
│   ├── producto_servicio.py
│   └── usuario_servicio.py
│
├── main.py
└── README.md
```

### Organización por módulos

- **entidades:** contiene las clases que representan los elementos principales del sistema.
- **servicios:** contiene la lógica de gestión y las operaciones sobre las entidades.
- **consola:** administra la interacción con el usuario mediante menús.
- **enums:** define los valores enumerados utilizados por el sistema.
- **excepciones:** contiene las excepciones personalizadas.
- **main.py:** inicializa los servicios y ejecuta el programa.

## Instalación y ejecución

### Requisitos

- Tener instalado Python 3.
- Descargar o clonar este repositorio.

### Ejecutar la aplicación

Desde la carpeta principal, ejecutar:

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

## Usuarios de prueba

El programa crea automáticamente un administrador y un cliente de prueba al iniciarse.

| Rol | Correo electrónico | Contraseña |
|---|---|---|
| Administrador | admin@foodstore.com | admin123 |
| Cliente | juan@foodstore.com | juan123 |

**Importante:** estas credenciales son únicamente para probar la aplicación.

## Autores

Trabajo Práctico Integrador realizado para la materia **Programación II**.

**Integrantes:**
- Leandro Morales
- Mateo Falcioni

## Enlaces

- **Video de presentación:** __________________________________
- **Enlace PDF:** __________________________________

## Bibliografía y documentación

- [Documentación oficial de Python](https://docs.python.org/3/)
- [Módulo abc — Clases abstractas](https://docs.python.org/3/library/abc.html)
- [Módulo enum — Enumeraciones](https://docs.python.org/3/library/enum.html)
- [Excepciones integradas de Python](https://docs.python.org/3/library/exceptions.html)
- [Módulo typing — Anotaciones de tipos](https://docs.python.org/3/library/typing.html)
