import sys
from collections import deque

if __name__ == '__main__':
    n = int(input())
    queue = deque()

    for _ in range(n):
        actions = sys.stdin.readline()
        action_list = actions.split()
        action = action_list[0]
        if action == 'push':
            queue.append(action_list[1])
        elif action == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
        elif action == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif action == 'back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
        elif action == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif action == 'size':
            print(len(queue))
