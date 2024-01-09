from prac.stack import Stack


class NodeWithMin(object):
    def __init__(self, value=None, minimum=None):
        self.value = value
        self.minimum = minimum


class StackMin(Stack):
    def __init__(self):
        super().__init__()
        self.items = []
        self.min = None

    def push(self, item):
        if self.is_empty() or self.min > item:
            self.min = item
        self.items.append(NodeWithMin(item, self.min))

    def peek(self):
        return self.items[-1].value

    def peek_minimum(self):
        return self.items[-1].minimum

    def pop(self):
        item = self.items.pop()
        if item:
            if item.value == self.min:  # pop 한 item 이 최소값일 경우
                self.min = self.peek_minimum()  # 나머지 값들 중 최소값 찾아내기
            return item.value
        else:
            print("Stack is empty")

    def __repr__(self):
        aux = []
        for i in self.items:
            aux.append(i.value)
        return repr(aux)


if __name__ == '__main__':
    """ 스택에서 최솟값 O(1) 로 조회하기 """
    stack = StackMin()
    for i in range(10, 0, -1):
        stack.push(i)

    for i in range(1, 5):
        stack.push(i)
    print(stack)

    print("peek: {0}".format(stack.peek()))
    print("peek_minimum: {0}".format(stack.peek_minimum()))
    print("pop: {0}".format(stack.pop()))
    print("peek: {0}".format(stack.peek()))
    print("peek_minimum: {0}".format(stack.peek_minimum()))

    print(stack)
