#Herança Multipla 

class Funcionario:

    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas Registradas...')
    
    def mostrar_tarefas(self):
        print('Fez Muita Coisa')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')
    
    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando Cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

#MIXIN
class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior('Jose')
jose.busca_perguntas_sem_resposta()


luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

#MRO Algorithm
#pleno > Alura > Caelum > Funcionario

#MIXIN
joao = Senior('João')

print(joao)