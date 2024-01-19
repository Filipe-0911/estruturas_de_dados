class No:
    def __init__(self, nome, proximo=None):
        self.__nome = nome
        self.__proximo = proximo
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def proximo(self):
        return self.__proximo
    
    @proximo.setter
    def proximo(self, novo_proximo):
        self.__proximo = novo_proximo