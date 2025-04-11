from administrador import Administrador


if __name__ == "__main__":
    admin = Administrador("Jorge", 123)
    print(admin.nombre)
    admin.nombre = "Juan"
    print(admin.nombre)
    admin2 = Administrador("Jorge", 123)
    print(admin2.nombre)
