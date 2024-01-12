from prac.linked_list import LinkedListFIFO


def part_list(linked_list, n):
    more = LinkedListFIFO()
    less = LinkedListFIFO()

    node = linked_list.head  # 연결리스트의 첫번째 값

    while node:  # 연결리스트를 순회
        item = node.value

        if item < n:  # 값이 n 보다 작으면 less 연결리스트에 넣어준다.
            less.add_node(item)
        elif item > n:  # 값이 n 보다 크면 more 연결리스트에 넣어준다.
            more.add_node(item)
        node = node.pointer  # 다음 값

    less.add_node(n)  # 마지막으로 less 에 n 을 넣어준다.
    nodemore = more.head

    while nodemore:  # more 연결리스트 값를 순회하면서 less 연결리스트에 넣어준다
        less.add_node(nodemore.value)
        nodemore = nodemore.pointer

    return less


if __name__ == "__main__":
    """ 연결 리스트 분할하기 """
    linked_list = LinkedListFIFO()
    l = [3, 4, 6, 3, 7, 9, 2, 1]
    for i in l:
        linked_list.add_node(i)

    linked_list.print_list()

    print('분할 후')
    part_ll = part_list(linked_list, 6)
    part_ll.print_list()
