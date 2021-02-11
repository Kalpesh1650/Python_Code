
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

list1 = list(arr)
'''list1.sort(reverse=True)
print(list1[1])'''

new_list = set(list1)

# removing the largest element from temp list
new_list.remove(max(new_list))

# elements in original list are not changed
# print(list1)

print(max(new_list))