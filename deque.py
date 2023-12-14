#deque ou fila duplamente ligada

class Deque:
    def __init__(self, deque=[], tamanho=0):
        self.deque = deque
        self.tamanho = tamanho

    def adicionar_no_fim(self, item):
        self.deque.append(item)
        self.tamanho += 1
    
    def adicionar_no_inicio(self, item):
        self.deque.insert(0, item)
        self.tamanho += 1
    
    def remover_do_inicio(self):
        self.deque.pop(0)
        self.tamanho -= 1
    
    def remover_do_fim(self):
        self.deque.pop(self.tamanho -1)
        self.tamanho -= 1

    def mostrar_itens(self):
        for index, item in enumerate(self.deque):
            print(f"Item{item} no índice {index}")