#Copying Files

#Used to copy file
# shutil.copy(src,dst)

#Used to copy file metadata information (MAC times, permissions)
# shutil.copystat(src,dst)

import shutil

#src = "demo.txt"
#dst = "DavesDemo.txt"
#shutil.copy(src,dst)



#renaming files

import os

#os.rename("lukademo.txt", "cooldemo.txt")

#os.remove("file.txt")   -  used to delete files



#PRACTICE TIME

#src = "baddydan.txt"
#dst = "badderz.txt"

#shutil.copy(src, dst)

#os.rename("badderz.txt", "badderino.txt")

#x = open("badderino.txt")
#print(x.read())
#x.close()

#___________________________________________________________


a = open("practice162.txt", "x")
a.write("This is the first line of text \n" + "This is the second line of text")
a.close()

src  = "practice162.txt"
dst = "demo.txt"

shutil.copy(src, dst)

a = open("demo.txt", "a")
a.write("Haha cools news texts added to files \n" + "This is so cool that this is possible")
a.close()

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

with open("practice162.txt") as myfile:
    contents = myfile.read()
    print(contents)














