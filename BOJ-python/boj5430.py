import re
import sys
from collections import deque

if __name__ == '__main__':
    t = int(sys.stdin.readline())

    for _ in range(t):
        command = sys.stdin.readline()
        n = int(sys.stdin.readline())
        arr = sys.stdin.readline()
        error = False
        reverse = 0
        queue = deque([s for s in re.findall(r'\d+', arr)])

        for p in command:
            if p == 'R':
                reverse += 1
            elif p == 'D':
                if len(queue) < 1:
                    print("error")
                    error = True
                    break
                if reverse % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
        if error is not True:
            if reverse % 2 == 0:
                print("[" + ",".join(queue) + "]")
            else:
                queue.reverse()
                print("[" + ",".join(queue) + "]")

