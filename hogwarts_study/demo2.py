
# f = open('data.txt')
# print(f.readable())
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()
# with可以将文件打开读取后自动关闭
with open('data.txt') as f:
    while True:
        line=f.readline()
        if line:
            print(line)
        else:
            break



