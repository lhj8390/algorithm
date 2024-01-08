from prac.stack import Stack


def reverse_string_with_stack(string):
    """ 문자열 반전하기 """
    s = Stack()
    reverse_str = ''

    for st in string:
        s.push(st)

    while not s.is_empty():
        reverse_str += s.pop()

    return reverse_str


if __name__ == '__main__':
    str1 = '테스트'
    print(str1)
    print(reverse_string_with_stack(str1))