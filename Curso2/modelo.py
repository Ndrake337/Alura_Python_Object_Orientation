class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes +=1

    #metodo __str__ permite que retornemos a representação textual de um objeto
    def __str__(self):
        return f'{self._nome} - {self.ano} - : {self._likes} Likes'
#Colocamos entre parenteses no nome da classe a heranças da classe
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #funçaõ super() me permite chamar um construtor ou metodo da classe mãe 
        super().__init__(nome, ano)
        self.duracao = duracao

    #metodo __str__ permite que retornemos a representação textual de um objeto
    def __str__(self):
        return f'{self._nome} - Ano: {self.ano} - {self.duracao} Minutos - : {self._likes} Likes'

#Colocamos entre parenteses no nome da classe a heranças da classe
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        #funçaõ super() me permite chamar um construtor ou metodo da classe mãe 
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} - Ano: {self.ano} - {self.temporadas} Temporadas - : {self._likes} Likes'

#exemplo Herdando dados da classe list, evitando uma série de códigos
# class Playlist(list):
#     def __init__(self, nome, programas):
#         self.nome = nome
#         super().__init__(programas)

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #Duck Typing
    #Outra forma de herança através de Composição, AO INVÉS DE DIZER QUE PLYALIST É UM LIST
    #PLAYLIST Tem um list
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    
    #através desse metodo a lista pode informar seu tamanho com o metodo len
    def __len__(self):
        return len(self._programas)

vingadores = Filme("Vingadores Guerra Infinita",2018,160)
atlanta = Serie("Atlanta",2018,2 )
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
   print(programa)

print(f'ta ou não tá ? {demolidor in playlist_fim_de_semana}')