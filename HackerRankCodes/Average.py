import os
import sys


def avg(*listofnumber):
    return sum(listofnumber) / len(listofnumber)


# user_input = input().split(' ')

# strip is used to remove the white space. Not mandatory

# all_numbers = [int(x.strip()) for x in user_input]
# #for i in all_numbers:
#     # print(i)
#
# print(" %0.2f " % avg(all_numbers))
fptr = sys.stdout

nums = list(map(int, input().split()))
res = avg(*nums)

fptr.write('%.2f' % res + '\n')

fptr.close()
#if __name__ == '__main__':

