import textwrap


def wrap(string1, max_width1):

    for i in range(0, len(string1), max_width1):
        for j in range(max_width):
            str = str + string1[j]
            
    return


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)