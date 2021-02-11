def mutate_string(string, position, character):

    str1 = ""
    for count in range(len(string)):
        char = string[count]
        if count == position:
            str1 = str1 + character
        else:
            str1 = str1 + string[count]
        # print(string[count])

    return str1


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)