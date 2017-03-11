from collections import deque
class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, item):
        self.q.appendleft(item)

    def dequeue(self):
        return self.q.pop()

    def isEmpty(self):
        return not self.q