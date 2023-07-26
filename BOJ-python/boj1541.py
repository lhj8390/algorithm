import re

if __name__ == '__main__':
    data = input()
    data = re.split('\\+-', data)
    print(data)