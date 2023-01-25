class BaseDeDados:
    # Metodo Construtor
    def __init__(self):
        self.__dados = {}

    # Metodo especial getter
    @property
    def dados(self):
        return self.__dados

    # Metodo especial setter (NAO CRIADO PORQUE O ATRIBUTO E PRIVADO)

    # Metodos
    def inserir_cliente(self, identificacao, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {identificacao: nome}
        else:
            self.__dados['clientes'].update({identificacao: nome})

    def lista_clientes(self):
        for identificacao, nome in self.__dados['clientes'].items():
            print(f'{identificacao} - {nome}')

    def apaga_cliente(self, identificacao):
        del self.__dados['clientes'][identificacao]
