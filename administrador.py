class Administrador():
    instancia = None
    def __new__(cls, nombre, contrasenia):
        if cls.instancia is None:
            cls.instancia = super(Administrador, cls).__new__(cls)
            cls.instancia.nombre = nombre
            cls.instancia.contrasenia = contrasenia
        return cls.instancia