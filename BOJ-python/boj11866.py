from collections import deque

if __name__ == '__main__':
    n, k = map(int, input().split())

    queue = deque([i for i in range(1, n + 1)])
    result = []

    while queue:
        queue.rotate(-(k - 1))
        result.append(str(queue.popleft()))

    print('<' + ', '.join(result) + '>')
