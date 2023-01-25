from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = datetime.now().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} nao pode comer porque esta falando!')
        else:
            if self.comendo:
                print(f'{self.nome} ja esta comendo!')
            else:
                print(f'{self.nome} esta comendo {alimento}!')
                self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} NAO esta comendo!')
        else:
            print(f'{self.nome} parou de comer!')
            self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} NAO pode falar agora porque esta comendo!')
        else:
            if self.falando:
                print(f'{self.nome} ja esta falando!')
            else:
                print(f'{self.nome} esta falando sobre {assunto}!')
                self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} NAO esta falando!')
        else:
            print(f'{self.nome} parou de falar!')
            self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        identificacao = randint(10000, 99999)
        return identificacao
