#A classe serve como uma planta ou receita para construir nosso objeto

#Classes tem que ser coesas, tendo apenas uma responsabilidade para se 

#Regra de coesão 
# S - Single responsibility principle
# O - Open/closed principle
# L - Liskov substitution principle
# I - Interface segregation principle
# D - Dependency inversion principle

class Conta:
    
    #função construtora, self é a referencia para encontrar o endereço de memória do objeto
    def __init__(self,numero, titular, saldo, limite):
        print("Construindo um objeto ... {}".format(self))
        
        #definindo o atributos (com o __ na frente do nome do atributo definimos que o mesmo é privado, embora ainda pode ser acessado)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
    #métodos representam tudo que o objeto pode fazer
    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.__saldo,self.__titular))
    
    def deposita(self,valor):
        self.__saldo += valor
    
    #criando métodos privados, da mesma forma que criamos atributos privados
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar<=valor_disponivel


    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O Valor R${} ultrapassa o limite disponivel para sua conta".format(valor))
    #utilizando o encapsulamento, usando o self o usuário pode acessar todos os métodos além dos atributos de um objeto
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #getters e setters , métodos que devolvem ou modificam um atributo do objeto, sem lidar diretamente com esse atributo
    #utilizamos a nomenclatura get e set como padrão (BOAS PRATICAS)
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite
    
    @property
    def saldo(self):
        return self.__saldo
    
    #só podemos criar setters para property's que ja tenham sido criadas
    @property
    def limite(self):
        return self.__limite
    
    @property
    def titular(self):
        return self.__titular
    

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    #métodos estáticos, são métodos que são da classe, que podemos inclusive chamar mesmo sem ter objetos criados
    @staticmethod
    def codigo_banco():
        return "001"

    #métodos estáticos, são métodos que são da classe, que podemos inclusive chamar mesmo sem ter objetos criados
    #só faz sentidos para atributos estáticos, usar este tipo de método em vão nos tira do mundo orientado a objetos
    @staticmethod
    def codigos_dos_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}