from prac.stack import Stack


def balance_parenthesis_str_stack(str1):
    """ 괄호 짝 확인하기 """
    s = Stack()
    is_balanced = True

    for st in str1:
        if st == "(":
            s.push(st)
        else:
            if not s.is_empty():
                s.pop()
            else:
                is_balanced = False
    if is_balanced and s.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(balance_parenthesis_str_stack("((())"))
    print(balance_parenthesis_str_stack("((()))"))
