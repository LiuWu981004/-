class Deque(object):
    def __init__(self):
        self._deque = []

    def add_front(self,value):
        self._deque.insert(0,value)

    def add_rear(self,value):
        self._deque.append(value)


    def pop_front(self):
        return self._deque.pop(0)
    def pop_rear(self):
        return self._deque.pop()

    def is_empty(self):
        return self._deque ==[]

    def size(self):
        return len(self._deque)
