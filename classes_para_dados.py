from dataclasses import dataclass, field


# Classe normal
class PessoaAntigo:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def __str__(self):
        class_str = f'{self.__class__.__name__}({self.nome} {self.sobrenome})'
        return class_str

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.sobrenome == other.sobrenome


# Dataclass
@dataclass(frozen=True)
class Pessoa:
    nome: str
    sobrenome: str
    ativo: bool = False
    enderecos: list = field(default_factory=list, repr=True, compare=True, kw_only=True)
    nome_completo: str = field(default='Missing', init=False, repr=True)

    def __post_init__(self):
        nome_completo = f'{self.nome} {self.sobrenome}'
        object.__setattr__(self, 'nome_completo', nome_completo)  # gambiarra, classe esta congelada

    