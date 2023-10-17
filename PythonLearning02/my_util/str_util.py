def str_reverse(s):
    s = s[::-1]
    return s


def substr(s, x, y):
    return s[x:y]


if __name__ == '__main__':
    s = 'hello'
    s = str_reverse(s)
    print(s)
    s = substr(s, 1, 4)
    print(s)
