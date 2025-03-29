#A palavra-chave usada para acessar propriedades e métodos de uma classe estando dentro dela é: c) A palavra-chave self

class Usuario:
    primeiroNome = ""
    ultimoNome = ""

    def hello(self):
        return f"Olá, {self.primeiroNome}"

usuario1 = Usuario()
usuario1.primeiroNome = "Jonnie"
usuario1.ultimoNome = "Bravo"

print(usuario1.hello())
