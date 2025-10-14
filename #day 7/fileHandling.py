"""
1) open a file
2) read/write 
3) close a file

File opening modes

r,w,a
r+,w+,a+
r= read if file exist
w = write if not exist create a file if exist so erase the file data and write .
a = exist file data ke aage write hoga
"""
# for rename existing file 
import os
# write in file
def write_to_file(filename,name):
    # f=open(filename,'w')
    # f.write(name)
    # f.close()
# use of with keyword
    with open(filename,'w') as f:
        f.write(name)
        
# append to file
def append_to_file(filename,name):
    f=open(filename,'a')
    f.write('\n')
    f.write(name)
    f.close()

# reading permoing for a file data
def read_from_file(filename):
    try:
        f=open(filename,'r')
        text=f.read()
        print(text)
    except FileNotFoundError:
        print("File not found")


def main():
    # name=input("enter your name")
    # write_to_file('file1.txt',name)
    # append_to_file('file1.txt',name)
    # read_from_file('file1.txt')
    os.rename("file2.txt","file1.txt")

main()
