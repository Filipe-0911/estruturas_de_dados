from ListaLigada.No import No

class ListaLigada(No):
    
    def __init__(self):
        self.primeiro = None
        self.__tamanho = 0
    
    def append(self, elemento):
        if self.primeiro:
            ponteiro = self.primeiro
            while ponteiro.proximo:
                ponteiro = ponteiro.proximo
            
            ponteiro.proximo = No(elemento)
        else:
            self.primeiro = No(elemento)
        
        self.__tamanho += 1

    def __len__(self):
        return self.tamanho
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    def __getitem__(self, index):
        ponteiro = self.__get_no(index)
              
        if ponteiro:
            return ponteiro.nome
        else:         
            raise IndexError("list index out of range")

    def __setitem__(self, index, elemento):
        ponteiro = self.__get_no(index)
              
        if ponteiro:
            ponteiro.nome = elemento
        else:
            raise IndexError("list index out of range")
    
    def index(self, elemento):
        ponteiro = self.primeiro
        i = 0
        while ponteiro:
            if ponteiro.nome == elemento:
                return i
            else:
                ponteiro = ponteiro.proximo
                i = i+1
        raise ValueError(f"{elemento} is not in list")
    
    def insert(self, index, elemento):
        no = No(elemento)
        if index == 0:
            no.proximo = self.primeiro
            self.primeiro = no
        else:
            ponteiro = self.__get_no(index - 1)
            no.proximo = ponteiro.proximo
            ponteiro.proximo = no
        
        self.__tamanho += 1

    def __get_no(self, index):
        ponteiro = self.primeiro
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("list index out of range")
        return ponteiro
    
    def remove(self, elemento):
        if self.primeiro == None:
            raise ValueError(f"{elemento} is not in list")
        elif self.primeiro.nome == elemento:
                self.primeiro = self.primeiro.proximo
                self.__tamanho -= 1
                return True
        else:
            antecedente = self.primeiro
            ponteiro = self.primeiro.proximo

            while ponteiro:
                if ponteiro.nome == elemento:
                    antecedente.proximo = ponteiro.proximo
                    ponteiro.proximo = None
                antecedente = ponteiro
                ponteiro = ponteiro.proximo
            self.__tamanho -= 1
            return True
        raise ValueError(f"{elemento} is not in list")
    
    def __repr__(self):
        r = ""
        ponteiro = self.primeiro
        while ponteiro:
            r = r + str(ponteiro.nome) + ", "
            ponteiro = ponteiro.proximo
        return r

    def __str__(self):
        return self.__repr__()

        



