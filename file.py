# wap to count the frequency of a character in given file . c
# can you use character frequency to tell whether the give program file is python file ,c file ,text file

import os
a = 0
file=open("firstfile.txt")
for i in file:
    for j in range(0,len(i)):
        a+=1
        
        print("count : ",a)

        filename,file=os.path.splitext("firstfile.txt")

        print("file_extension",file)

        if(file==".py"):
            print("it is a python file")
        elif(file==".txt"):
            print("it is a text file")
        elif(file==".c"):
            print("it is a c file")
        else:
            print("no file found")
