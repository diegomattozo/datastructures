class Empty(Exception):
    pass


class ArrayQueue:
    """implementacao de uma fila usando listas do python"""
    DEFAULT_CAPACITY = 5

    def __init__(self):
        """cria uma fila vazia"""
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        """retorna o numero de elementos na fila"""
        return self._size

    def is_empty(self):
        """retorna true se a fila estiver vazia"""
        return self._size == 0

    def first(self):
        """retorna primeiro elemento da fila (sem remove-lo).
        se a queue estiver vazia retorna um erro"""
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[self._front]

    def dequeue(self):
        """remove e retorna o primeiro elemento na fila"""
        if self.is_empty():
            raise Empty('Queue is empty.')
        
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """adiciona uma elemento no fim da fila"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """aumenta a capacidade da lista"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

fila = ArrayQueue()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(4)
fila.enqueue(4)
fila.enqueue(4)
fila.enqueue(4)
fila.enqueue(4)

print("primeiro elemento", fila.first())
print("removendo primeiro elemento da fila", fila.dequeue())
print("removendo segundo elemento da fila", fila.dequeue())