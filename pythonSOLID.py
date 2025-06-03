import datetime

# --- Entidades ---
class Usuario:
    def __init__(self, nombre, email, tipo):
        self.nombre = nombre
        self.email = email
        self.tipo = tipo


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# --- Lógica de Descuentos ---
class EstrategiaDescuento:
    def calcular(self, producto):
        return producto.precio

class DescuentoVip(EstrategiaDescuento):
    def calcular(self, producto):
        return producto.precio * 0.8

class DescuentoEstudiante(EstrategiaDescuento):
    def calcular(self, producto):
        return producto.precio * 0.9

class DescuentoJubilado(EstrategiaDescuento):
    def calcular(self, producto):
        return producto.precio * 0.85

class CalculadoraDescuentos:
    estrategias = {
        "vip": DescuentoVip(),
        "estudiante": DescuentoEstudiante(),
        "jubilado": DescuentoJubilado(),
        "normal": EstrategiaDescuento()
    }

    @staticmethod
    def obtener(tipo_usuario):
        return CalculadoraDescuentos.estrategias.get(tipo_usuario, EstrategiaDescuento())

# --- Manejo de Datos ---
class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar(self, nombre, email, tipo):
        usuario = Usuario(nombre, email, tipo)
        self.usuarios.append(usuario)
        return usuario

    def buscar_por_email(self, email):
        return next((u for u in self.usuarios if u.email == email), None)


class GestorProductos:
    def __init__(self):
        self.productos = []

    def agregar(self, nombre, precio):
        producto = Producto(nombre, precio)
        self.productos.append(producto)
        return producto

# --- Utilidades ---
class Logger:
    def __init__(self):
        self.logs = []

    def guardar(self, mensaje):
        self.logs.append(mensaje)
        with open("logs.txt", "a") as f:
            f.write(mensaje + "\n")

    def mostrar(self):
        for log in self.logs:
            print(log)


class EmailService:
    def __init__(self, logger):
        self.logger = logger

    def enviar(self, email, mensaje):
        print(f"[EMAIL SIMULADO] Enviando a {email}: {mensaje}")
        self.logger.guardar(f"{datetime.datetime.now()} - Email enviado a {email}: {mensaje}")

# --- Facturación ---
class SistemaFacturacion:
    def __init__(self, gestor_usuarios, gestor_productos, logger):
        self.gestor_usuarios = gestor_usuarios
        self.gestor_productos = gestor_productos
        self.logger = logger

    def mostrar_factura(self, email_usuario):
        usuario = self.gestor_usuarios.buscar_por_email(email_usuario)
        if not usuario:
            print("Usuario no encontrado")
            return

        print("\n=== FACTURA ===")
        print("Cliente:", usuario.nombre)
        total = 0
        estrategia = CalculadoraDescuentos.obtener(usuario.tipo)

        for producto in self.gestor_productos.productos:
            precio_final = estrategia.calcular(producto)
            print(f"- {producto.nombre}: ${precio_final:.2f}")
            total += precio_final

        print("TOTAL A PAGAR:", total)
        self.logger.guardar(f"{datetime.datetime.now()} - Factura generada para {usuario.nombre} por ${total:.2f}")

# --- Interfaz de Usuario ---
class Aplicacion:
    def __init__(self):
        self.logger = Logger()
        self.gestor_usuarios = GestorUsuarios()
        self.gestor_productos = GestorProductos()
        self.facturacion = SistemaFacturacion(self.gestor_usuarios, self.gestor_productos, self.logger)
        self.email_service = EmailService(self.logger)

    def menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Registrar usuario")
            print("2. Agregar producto")
            print("3. Mostrar factura")
            print("4. Enviar email")
            print("5. Ver logs")
            print("0. Salir")

            opcion = input("Seleccionar opción: ")
            if opcion == "1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                tipo = input("Tipo de usuario (normal/vip/estudiante/jubilado): ")
                self.gestor_usuarios.registrar(nombre, email, tipo)
                self.logger.guardar(f"{datetime.datetime.now()} - Usuario {nombre} registrado")
            elif opcion == "2":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio del producto: "))
                self.gestor_productos.agregar(nombre, precio)
                self.logger.guardar(f"{datetime.datetime.now()} - Producto {nombre} agregado")
            elif opcion == "3":
                email = input("Email del usuario: ")
                self.facturacion.mostrar_factura(email)
            elif opcion == "4":
                email = input("Email destino: ")
                mensaje = input("Mensaje: ")
                self.email_service.enviar(email, mensaje)
            elif opcion == "5":
                print("\n--- LOGS ---")
                self.logger.mostrar()
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida")

# --- Ejecución principal ---
if __name__ == "__main__":
    app = Aplicacion()
    app.menu()
