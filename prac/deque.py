from queues import Queue


class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print("Deque is empty.")


if __name__ == "__main__":
    deque = Deque()
    for i in range(10):
        deque.enqueue(i)

    print("peek: {0}".format(deque.peek()))
    print("dequeue: {0}".format(deque.dequeue()))
    print("peek: {0}".format(deque.peek()))
    print()
    print("deque: {0}".format(deque))
    print("dequeue: {0}".format(deque.dequeue_front()))
    print("peek: {0}".format(deque.peek()))
    print("deque: {0}".format(deque))

    print("enqueue_back(50)")
    deque.enqueue_back(50)
    print("peek: {0}".format(deque.peek()))
    print("deque: {0}".format(deque))