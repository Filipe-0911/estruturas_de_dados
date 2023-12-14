class Pilha:
    def __init__(self, pilha=[], tamanho=0):
        self.pilha = pilha
        self.tamanho = tamanho
    
    def adicionar_no_inicio(self, nome_do_jogo):
        self.pilha.insert(0, nome_do_jogo)
        self.tamanho += 1
    
    def mostrar_itens(self):
        for index, item in enumerate(self.pilha):
            print(f"Item{item} no índice {index}")

    def quantidade_de_itens(self):
        return self.tamanho
    
    def remover_do_inicio(self):
        self.pilha.pop(0)
        self.tamanho -= 1