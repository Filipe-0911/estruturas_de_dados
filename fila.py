class Fila:
    def __init__(self, fila=[], tamanho=0):
        self.fila = fila
        self.tamanho = tamanho
    
    def adicionar_no_fim(self, nome_do_jogo):
        self.fila.append(nome_do_jogo)
        self.tamanho += 1
    
    def mostrar_itens(self):
        for index, item in enumerate(self.fila):
            print(f"Item{item} no índice {index}")

    def quantidade_de_itens(self):
        return self.tamanho
    
    def remover_do_inicio(self):
        self.fila.pop(0)
        self.tamanho -= 1