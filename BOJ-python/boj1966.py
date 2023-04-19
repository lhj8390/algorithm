from collections import deque

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        queue = deque(list(map(int, input().split())))
        idx = deque(range(n))  # index 값 같이 저장
        order = 0
        while queue:
            priority = max(queue)
            doc = queue.popleft()
            now_idx = idx.popleft()
            if doc == priority:
                order += 1
                if now_idx == m:
                    print(order)
            else:
                queue.append(doc)
                idx.append(now_idx)
