from prac.linked_list import LinkedListFIFO


class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._create_hash_table()

    def _create_hash_table(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())

    def _find(self, item):
        return item % self.size

    def add(self, item):
        index = self._find(item)
        self.slots[index].add_node(item)

    def delete(self, item):
        index = self._find(item)
        self.slots[index].delete_node_by_value(item)

    def print(self):
        for i in range(self.size):
            print("슬롯(slot) {0}: ".format(i))
            self.slots[i].print_list()


if __name__ == '__main__':
    h1 = HashTableLL(3)
    for i in range(0, 20):
        h1.add(i)

    h1.print()
    h1.delete(0)
    h1.delete(1)
    h1.delete(2)
    print()
    h1.print()
