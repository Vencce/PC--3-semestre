class Usuario:
    def __init__(self):
        self.__nomeUsuario = None

    def set_nomeUsuario(self, nome):
        self.__nomeUsuario = nome

    def get_nomeUsuario(self):
        return self.__nomeUsuario

class Admin(Usuario):
    def escrevaNome(self):
        return "Admin"

    def digaOla(self):
        return f"Olá Admin, {self.get_nomeUsuario()}"


admin1 = Admin()
admin1.set_nomeUsuario("Baltazar")
print(admin1.digaOla())


#8-Atributos privados (__nomeUsuario) não são acessíveis diretamente por classes filhas.

