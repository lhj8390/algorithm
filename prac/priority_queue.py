import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "ITEM({0!r})".format(self.name)


if __name__ == '__main__':
    ''' push 와 pop 은 모두 O(logN)이다 '''

    q = PriorityQueue()
    q.push(Item('test1'), 1)
    q.push(Item('test2'), 4)
    q.push(Item('test3'), 3)

    assert str(q.pop()) == "ITEM('test2')"
    print("테스트 통과")
