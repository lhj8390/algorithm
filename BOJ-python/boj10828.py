import sys

if __name__ == '__main__':
    n = int(input())
    stack = []
    for _ in range(n):
        actions = sys.stdin.readline()
        action_list = actions.split()
        action = action_list[0]
        num = 0
        if len(action_list) > 1:
            num = int(action_list[1])

        # action
        if action == 'push':
            stack.append(num)
        elif action == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack) - 1])
        elif action == 'size':
            print(len(stack))
        elif action == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif action == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
