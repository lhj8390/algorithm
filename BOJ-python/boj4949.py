if __name__ == '__main__':
    while True:
        line = input()
        if line == '.':
            break
        stack = []
        first = '(['
        last = ')]'
        result = True
        for word in line:
            if len(stack) == 0 and word in last:
                result = False
                break
            if word in first:
                stack.append(word)
            elif word in last:
                if first.index(stack[-1]) == last.index(word):
                    stack.pop()
                else:
                    result = False
                    break
        if len(stack) != 0:
            result = False

        print('yes' if result else 'no')
