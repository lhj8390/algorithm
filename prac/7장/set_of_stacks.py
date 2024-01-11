from prac.stack import Stack


class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        super().__init__()
        self.setOfStacks = []
        self.capacity = capacity

    def push(self, item):
        if self.size() >= self.capacity:  # 정해진 용량을 초과할 경우
            self.setOfStacks.append(self.items)  # 기존 items 들을 별도의 배열에 저장하고
            self.items = []                      # item 배열을 초기화한다.
        self.items.append(item)

    def pop(self):
        value = self.items.pop()
        if self.is_empty() and self.setOfStacks:  # 기존 item 배열이 빌 경우
            self.items = self.setOfStacks.pop()  # 별도의 배열에서 값을 빼서 item 배열에 저장
        return value

    def total_size(self):
        return len(self.setOfStacks) * self.capacity + self.size()

    def __repr__(self):
        aux = []
        for s in self.setOfStacks:
            aux.extend(s)
        aux.extend(self.items)
        return repr(aux)


if __name__ == '__main__':
    """ 용량이 존재하는 Stack """
    s = SetOfStacks(capacity=5)
    for i in range(10):
        s.push(i)

    print(s)
    print("Stack size: {0}".format(s.total_size()))
    print("peek: {0}".format(s.peek()))
    print("pop: {0}".format(s.pop()))
    print("peek: {0}".format(s.peek()))
    print(s)