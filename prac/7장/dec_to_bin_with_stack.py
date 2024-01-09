from prac.stack import Stack


def dec_to_bin_with_stack(decnum):
    """ 10 진수를 2 진수로 변환 """
    s = Stack()
    str_num = ""

    while decnum > 0:
        dig = decnum % 2
        decnum = decnum // 2
        s.push(dig)

    while not s.is_empty():
        str_num += str(s.pop())

    return str_num


if __name__ == "__main__":
    decum = 9
    print(dec_to_bin_with_stack(decum))
