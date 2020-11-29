import os

# os.mkdir("test_dir")
# print(os.listdir("./"))
# os.rmdir("test_dir")

print(os.path.exists(""))
if not os.path.exists(""):
    os.mkdir("")

if not os.path.exists("./ku/test.txt"):
    f = open("./ku/test.txt", 'w')
    f.write("hello, os using ")
    f.close()

with open("./ku/test.txt", 'r')as d:
    print(d.readlines())

