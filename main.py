'''from pessoa35_36_37_39 import Pessoa
from produto38 import Produto
from basededados40 import BaseDeDados
from classes41 import Escritor, Caneta, MaquinaDeEscrever
from classes42 import CarrinhoDeCompras, Produto
from classes43 import Cliente
from classes44 import *
from classesparadados import *
from classesmetaclass import *'''

# AULA 35
'''p1 = Pessoa('Gabriel', 24)
p2 = Pessoa('Vitoria', 25)

p1.falar('POO')
p2.falar('Moda')
print(p1.get_ano_nascimento())
print(p1.ano_atual)'''

# AULA 36
'''p1 = Pessoa.por_ano_nascimento('Gabriel', 1998)
print(p1.idade)'''

# AULA 37
'''p1 = Pessoa('Gabriel', 24)
print(Pessoa.gera_id())
print(p1.gera_id())'''

# AULA 38
'''p1 = Produto('CaMIsEtA', 50)
p1.desconto(10)
print(p1.nome, ' - ', p1.preco)

p2 = Produto('CANeCa', 'R$15,98')
p2.desconto(10)
print(f'{p2.nome} - R${p2.preco:.2f}'.replace('.', ','))'''

# AULA 39
'''obj_1 = Pessoa('Gabriel', 24)
obj_2 = Pessoa('Vitoria', 25)

print(obj_1.ano_atual)
print(obj_2.ano_atual)
print(Pessoa.ano_atual)

obj_1.ano_atual = 2023
obj_2.ano_atual = 2025

print(obj_1.__dict__)
print(obj_2.__dict__)
print(Pessoa.__dict__)

Pessoa.ano_atual = 2021

print(obj_1.__dict__)
print(obj_2.__dict__)
print(Pessoa.__dict__)'''

# AULA 40
'''bd = BaseDeDados()
bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.apaga_cliente(2)

# Nao e possivel alterar o dicionario dados, pois ele esta privado
bd.__dados = 'Outra coisa'  # O dicionario original nao foi alterado
print(bd.__dados)  # Apenas foi criada nova variavel de nome __dados, independente

bd.lista_clientes()

# Para acessar o atributo privado (NAO USUAL)
print(bd._BaseDeDados__dados)

# Usando o getter para obter os dados do atributo privado
print(bd.dados)  # Teremos o mesmo resuldado do _BaseDeDados__dados'''

# AULA 41
'''escritor = Escritor('Joaozinho')
print(escritor.nome)
caneta = Caneta('BIC')
print(caneta.marca)
maquina = MaquinaDeEscrever()
maquina.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
maquina.escrever()
caneta.escrever()'''

# AULA 42
'''carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())'''

# AULA 43
'''c1 = Cliente('Luiz', 32)
c1.insere_endereco('Belo Horizonte', 'MG')
print(f'{c1.nome}\n', end=' ')
c1.lista_enderecos()
del c1
print()

c2 = Cliente('Maria', 55)
c2.insere_endereco('Salvador', 'BA')
c2.insere_endereco('Rio de Janeiro', 'RJ')
print(f'{c2.nome}\n', end=' ')
c2.lista_enderecos()
del c2
print()

c3 = Cliente('Joao', 19)
c3.insere_endereco('Sao Paulo', 'SP')
print(f'{c3.nome}\n', end=' ')
c3.lista_enderecos()
del c3
print()

print('#' * 40)'''

# AULA 44
'''c1 = Cliente('Luiz', 45)
c1.falar('Good morning! Do you have tomatoes? I want 5...')
c1.comprar('tomatoes')

a1 = Aluno('Joao', 54)
a1.falar("Professor, I didn't understand this sentence. Could you repeat, please?")
a1.estudar('English')

p1 = Pessoa('Antonio', 35)
p1.falar('Eu apenas posso falar, pois comprar e estudar sao metodos que apenas minhas filhas tem!')'''

# DATACLASSES
'''if __name__ == '__main__':
    joao1 = Pessoa('Joao', 'Silva', True, enderecos=['R1'])
    joao2 = Pessoa('Joao', 'Silva', True, enderecos=['R2'])
    print(joao1)
    print(joao2)
    print(joao1 == joao2)'''

# METACLASSES
'''person1 = Person('Luiz', 'Otavio')
person2 = Person('Maria', 'Oliveira')
num = 123
print(type(person1))
print(type(Person))
print(type(num ))
print(type(list))'''
