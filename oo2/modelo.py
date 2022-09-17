class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
       return f' {self._nome} - {self.ano} - {self._likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # super() é o inicializador da classe mãe
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.duracao} min - {self._likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.temporada} temp - {self._likes}'

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

tmep = Filme('todo mundo em pânico', 1999, 100)
tmep.dar_like()
demolidor = Filme('Demolidor', 2016, 2)
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'tamanho do playlist: {len(playlist_fim_de_semana)}')

len(playlist_fim_de_semana)

for programa in playlist_fim_de_semana.listagem:
    print(programa)
