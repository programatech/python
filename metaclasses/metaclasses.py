class MinhaMetaclasse(type):
    def __new__(cls, nome, bases, dct):
        # Adicionando um método em todas as classes
        dct['novo_metodo'] = lambda self: print(f"Olá do novo método em {self.__class__.__name__}!")
        return super().__new__(cls, nome, bases, dct)

# Usando a metaclasses
class MinhaClasse(metaclass=MinhaMetaclasse):
    def __init__(self, nome):
        self.nome = nome

# Testando
instancia = MinhaClasse("Exemplo")
instancia.novo_metodo()  # Saída: Olá do novo método em MinhaClasse!

