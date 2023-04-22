import sys
from collections import deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    queue = deque()

    for _ in range(n):
        actions = list(map(str, sys.stdin.readline().split()))

        if actions[0] == 'push_back':
            queue.append(int(actions[1]))
        elif actions[0] == 'push_front':
            queue.appendleft(int(actions[1]))
        elif actions[0] == 'pop_front':
            if len(queue) == 0:
                print(-1)
                continue
            print(queue.popleft())
        elif actions[0] == 'pop_back':
            if len(queue) == 0:
                print(-1)
                continue
            print(queue.pop())
        elif actions[0] == 'size':
            print(len(queue))
        elif actions[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif actions[0] == 'front':
            if len(queue) == 0:
                print(-1)
                continue
            print(queue[0])
        elif actions[0] == 'back':
            if len(queue) == 0:
                print(-1)
                continue
            print(queue[-1])
