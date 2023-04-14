from collections import deque

if __name__ == '__main__':
    n = int(input())
    queue = deque([i + 1 for i in range(n)])

    while len(queue) > 0:
        if len(queue) == 1:
            print(queue[0])
            break
        queue.popleft()  # 제일 위에 있는 카드를 바닥에 버린다.
        moved = queue.popleft()  # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
        queue.append(moved)

