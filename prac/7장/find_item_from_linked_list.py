from prac.linked_list import LinkedListFIFO


class FindItemFromLast(LinkedListFIFO):
    def find_item(self, item):
        h1, h2 = self.head, self.head
        i = 0
        while h1:
            if i > item - 1:
                if h2.pointer:
                    h2 = h2.pointer
                else:
                    break
            h1 = h1.pointer
            i += 1
        return h2.value


if __name__ == '__main__':
    """ 연결리스트 끝에서부터 n 번째 항목 찾기 """
    linked_list = FindItemFromLast()
    for i in range(8, 36):
        linked_list.add_node(i)

    linked_list.print_list()
    find_idx = 21
    idx_from_last = linked_list.find_item(find_idx)
    print("{0}번째 항목은 {1}".format(find_idx, idx_from_last))