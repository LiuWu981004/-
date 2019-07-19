class Queue(object):
    def __init__(self):
        self._queue = []

    def enqueue(self,value):
        self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def is_empty(self):
        return self._queue ==[]

    def size(self):
        return len(self._queue)

if __name__=='__main__':
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(5)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
