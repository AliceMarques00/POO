class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.comendo = False
        self.andando = False
        self.falando = False

    def comer(self, comida):
        self.parar_todas_acoes()
        self.comendo = True
        print(f'{self.nome} está agora comendo {comida}.')

    def falar(self, discurso):
        self.parar_todas_acoes()
        self.falando = True
        print(f'{self.nome} está agora falando: "{discurso}".')

    def andar(self, distancia):
        self.parar_todas_acoes()
        self.andando = True
        print(f'{self.nome} está agora andando {distancia} metros.')

    def parar_todas_acoes(self):
        if self.comendo:
            self.comendo = False
            print(f'{self.nome} parou de comer.')
        if self.falando:
            self.falando = False
            print(f'{self.nome} parou de falar.')
        if self.andando:
            self.andando = False
            print(f'{self.nome} parou de andar.')

pessoa = Pessoa("Alice")
pessoa.comer("peixe")
pessoa.andar('duzentos')
pessoa.falar("por favor agora vai")
pessoa.parar_todas_acoes()
