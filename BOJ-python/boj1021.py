from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque([i for i in range(1, n + 1)])
    cnt = 0
    for a in arr:
        while True:
            target = queue[0]
            if target != a:
                if queue.index(a) <= len(queue) // 2:
                    q = queue.popleft()
                    queue.append(q)
                    cnt += 1
                else:
                    q = queue.pop()
                    queue.appendleft(q)
                    cnt += 1
            else:
                queue.popleft()
                break

    print(cnt)
