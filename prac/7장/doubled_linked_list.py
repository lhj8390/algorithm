from prac.linked_list import LinkedListFIFO


class DoubleNode(object):
    def __init__(self, value=None, pointer=None, previous=None):
        self.value = value
        self.pointer = pointer
        self.previous = previous


class DoubledLinkedList(LinkedListFIFO):
    def print_list_inverse(self):
        node = self.tail
        while node:
            print(node.value, end=" ")
            if node and hasattr(node, "previous"):
                node = node.previous
            else:
                break
            print()

    def _add(self, value):
        self.length += 1
        node = DoubleNode(value)
        if self.tail:  # 마지막 요소가 존재할 경우
            self.tail.pointer = node  # 마지막 요소의 마지막 값을 현재 노드로 지정
            node.previous = self.tail  # 현재 노드의 이전 값을 마지막 요소로 지정
        self.tail = node

    def _delete(self, node):
        self.length -= 1
        node.previous.pointer = node.pointer  # 삭제하려는 노드의 이전 요소의 다음 값을 현재 노드의 마지막 값으로 변경
        if not node.pointer:
            self.tail = node.previous

    def _find(self, index):
        node = self.head
        i = 0
        while node and i < index:
            node = node.pointer
            i += 1
        return node, i

    def delete_node(self, index):
        if not self.head or not self.head.pointer:
            self._delete_first()
        else:
            node, i = self._find(index)
            if i == index:
                self._delete(node)
            else:
                print("index {0} 에 해당하는 노드가 없습니다".format(index))


if __name__ == '__main__':
    lists = DoubledLinkedList()
    for i in range(1, 5):
        lists.add_node(i)
    lists.print_list()
    print("reverse linked list")
    lists.print_list_inverse()

    lists.add_node(15)
    lists.print_list()
    for i in range(lists.length - 1, -1, -1):
        lists.delete_node(i)
    lists.print_list()
