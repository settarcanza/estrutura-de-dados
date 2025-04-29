from ListasEncadeadas.node import Node

class ListaSimples:
    """Implementação de uma lista encadeada simples."""

    def __init__(self):
        """Inicializa uma lista encadeada vazia."""
        self.head = None

    def is_empty(self) -> bool:
        """Verifica se a lista está vazia."""
        return self.head is None

    def insere_inicio(self, item: any) -> None:
        """Insere um novo nó no início da lista."""
        novo_node = Node(item)
        novo_node.next = self.head
        self.head = novo_node

    def insere_fim(self, item: any) -> None:
        """Insere um novo nó no final da lista."""
        novo_node = Node(item)
        if self.is_empty():
            self.head = novo_node
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = novo_node

    def remove_inicio(self) -> any:
        """Remove e retorna o item do início da lista."""
        if self.is_empty():
            raise Exception("Lista vazia!")
        removido = self.head
        self.head = self.head.next
        return removido.item

    def remove_item(self, item: any) -> bool:
        """Remove a primeira ocorrência do item na lista. Retorna True se removido, False caso contrário."""
        atual = self.head
        anterior = None
        while atual:
            if atual.item == item:
                if anterior:
                    anterior.next = atual.next
                else:
                    self.head = atual.next
                return True
            anterior = atual
            atual = atual.next
        return False

    def busca(self, item: any) -> Node | None:
        """Busca e retorna o nó contendo o item, ou None se não encontrado."""
        atual = self.head
        while atual:
            if atual.item == item:
                return atual
            atual = atual.next
        return None

    def imprime_lista(self) -> None:
        """Imprime os itens da lista no formato: item1 -> item2 -> ... -> None."""
        elementos = []
        atual = self.head
        while atual:
            elementos.append(str(atual.item))
            atual = atual.next
        print(" -> ".join(elementos) + " -> None")
