class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

    def get_data(self):
        return self.value

    def get_next(self):
        return self.pointer

    def set_data(self, new_data):
        self.value = new_data

    def set_next(self, new_pointer):
        self.pointer = new_pointer


class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    # 헤드부터 각 노드의 값 출력
    def print_list(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()

    # 이전 노드를 기반으로 노드를 삭제한다.
    def _delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

    # 새 노드를 추가한다. 다음 노드로 head 를 가리키고 head 는 새 노드를 가리킨다.
    def add(self, value):
        self.length += 1
        self.head = Node(value, self.head)

    # index 로 노드를 찾는다.
    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    # 값으로 노드를 찾는다
    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, found, prev

    # index 에 해당하는 노드를 찾아서 삭제한다.
    def delete_node(self, index):
        node, prev, i = self._find(index)
        if index == i:
            self._delete(prev, node)
        else:
            print(f"인덱스 {index}에 해당하는 노드가 없습니다.")

    # 값에 해당하는 노드를 찾아서 삭제한다.
    def delete_node_by_value(self, value):
        node, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev, node)
        else:
            print(f"값 {value}에 해당하는 노드가 없습니다.")


class LinkedListFIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    # head 부터 각 노드의 값 출력
    def print_list(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()

    # 첫 번째 위치에 노드 추가
    def _add_first(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node

    # 첫 번째 위치의 노드 삭제
    def _delete_first(self):
        self.length = 0
        self.head = None
        self.tail = None
        print('연결 리스트가 비었습니다.')

    # 새 노드 추가
    # tail 이 있다면 tail 의 다음 노드는 새 노드, tail은 새 노드를 가리킨다
    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

    # 새 노드 추가
    def add_node(self, value):
        if not self.head:
            self._add_first(value)
        else:
            self._add(value)

    # index 로 노드 찾기
    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    # 값으로 노드 찾기
    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    # index 에 해당하는 노드 삭제
    def delete_node(self, index):
        if not self.head or not self.head.pointer:
            self._delete_first()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("인덱스 {0}에 해당하는 노드가 없습니다".format(index))

    # 값에 해당하는 노드 삭제
    def delete_node_by_value(self, value):
        if not self.head or not self.head.pointer:
            self._delete_first()
        else:
            node, prev, i = self._find_by_value(value)
            if node and node.value == value:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("값 {0}에 해당하는 노드가 없습니다".format(value))


if __name__ == '__main__':
    L = Node("a", Node("b", Node("c", Node("d"))))
    assert L.pointer.pointer.value == "c"

    print(L.get_data())
    print(L.get_next().get_data())
    L.set_data("aa")
    L.set_next(Node("e"))
    print(L.get_data())
    print(L.get_next().get_data())

    LL = LinkedListLIFO()
    for i in range(1, 5):
        LL.add(i)
    LL.print_list()
    LL.delete_node(2)
    LL.print_list()
    LL.delete_node_by_value(3)
    LL.print_list()

    lf = LinkedListFIFO()
    for i in range(1, 5):
        lf.add_node(i)

    lf.print_list()
    lf.delete_node(2)
    lf.print_list()
    lf.add_node(15)
    lf.print_list()
