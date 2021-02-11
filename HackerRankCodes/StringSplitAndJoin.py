
def split_and_join(line):
    # write your code here
    #print(line)
    str1 = line.split(" ")
    str2 = ""
    for i in range(len(str1)-1):
        str2 = str2 + str1[i]+"-"
        # print(str1[i]+"-")

    print(str2+str1[len(str1)-1])


split_and_join("this is a string")

