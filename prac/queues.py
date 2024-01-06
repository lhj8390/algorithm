class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)  # 모든 요소가 메모리에서 이동될 수 있으므로 비효율적 (O(n))

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is empty")

    def __repr__(self):
        return repr(self.items)


class Queue2(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print("Queue is empty")

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            print("Queue is empty")

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print("Queue is empty")

    def is_empty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))


class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return not bool(self.head)

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print("Queue is empty")

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count += 1

    def size(self):
        return self.count

    def peek(self):
        return self.head.value

    def print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)

    print("peek: {0}".format(queue.peek()))
    print("dequeue: {0}".format(queue.dequeue()))
    print("peek: {0}".format(queue.peek()))
    print(queue)

    queue2 = Queue2()
    for i in range(10):
        queue2.enqueue(i)

    print("peek: {0}".format(queue2.peek()))
    print("dequeue: {0}".format(queue2.dequeue()))
    print("peek: {0}".format(queue2.peek()))
    print(queue2)

    queue3 = LinkedQueue()
    for i in range(10):
        queue3.enqueue(i)
    print("peek: {0}".format(queue3.peek()))
    print("dequeue: {0}".format(queue3.dequeue()))
    print("peek: {0}".format(queue3.peek()))
    queue3.print()
