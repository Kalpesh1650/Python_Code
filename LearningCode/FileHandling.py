
f = open('D:/Python WS/DataFiles/Data.txt','r') # open file in read mode

# print(f.readline()) # to read single line from file
print(f.read()) # to read complete file

""" to write to file """

f1 = open('D:/Python WS/DataFiles/FileToWrite.txt', 'w') # open file in write mode
f1.write("This is programmatically created file")
