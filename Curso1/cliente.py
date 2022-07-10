
class Cliente:

    def __init__(self, nome):
        self.__nome = nome
    
    #propriedades (properties), métodos que alteram atributos, só funciona com atributos privados
    #pode ser usado tanto em getters quanto em setters
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()
    
    @nome.setter
    def nome(self, nome ):
        print("chamando setter nome()")
        self.__nome = nome