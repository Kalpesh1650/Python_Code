def swap_case(s):
    for i in range (len(s)):
        if s[i].isupper():
             return s[i].lower()
        elif s[i].islower():
            return s[i].upper()
        else:
            return s[i]


def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    #swap_case(reverse_sentence)
    #print("".join(map(swap_case, reverse_sentence)))
    return reverse_sentence.swapcase()


s=input()
print(reverse_words_order_and_swap_cases(s))
# then reverse the split string list and join using space
# reverse_sentence = ' '.join(reversed(words))
# swap_case(reverse_sentence)
# print("".join(map(swap_case,reverse_sentence)))