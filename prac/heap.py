class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data) // 2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    @staticmethod
    def parent(i):
        if i % 2:
            return i // 2
        else:
            return (i // 2) - 1

    @staticmethod
    def left_child(i):
        return (i * 2) + 1

    @staticmethod
    def right_child(i):
        return (i * 2) + 2

    def __max_heapify__(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)

        # 왼쪽 자식
        largest = left if left < n and self.data[left] > self.data[i] else i
        # 오른쪽 자식
        largest = right if right < n and self.data[right] > self.data[largest] else largest

        # 현재 노드가 자식들보다 크다면 skip, 자식이 크다면 swap
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.__max_heapify__(largest)

    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]

        # 첫 번째 노드에 마지막 노드를 삽입
        self.data[0] = self.data[n - 1]
        self.data = self.data[:n - 1]
        self.__max_heapify__(0)
        return max_element

    def insert(self, item):
        i = len(self.data)
        self.data.append(item)
        while (i != 0) and item > self.data[self.parent(i)]:
            print(self.data)
            self.data[i] = self.data[self.parent(i)]
            i = self.parent(i)
        self.data[i] = item


if __name__ == '__main__':
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    assert h.extract_max() == 8
