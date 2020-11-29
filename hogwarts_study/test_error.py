# try:
#     num1 = int(input("请输入一个被除数"))
#     num2 = int(input("请输入一个除数"))
#     print(num1 / num2)
# # 0作为除数异常时抛出报错
# except ZeroDivisionError:
#     print("报错：0不能做除数")
# # 字符型数据输入异常时抛出报错
# except ValueError:
#     print("报错：除数必须为int型整数")
# # 程序正常运行时的返回结果
# else:
#     print("数据准确，程序执行正常")

"""
或者优化报错为通用性报错内容：如下
"""
# try:
#     num1 = int(input("请输入一个被除数"))
#     num2 = int(input("请输入一个除数"))
#     print(num1 / num2)
# except:
#     print("数据有误，除数不能为0，且数据不能为非int型数据")
# # 程序正常运行时的返回结果
# else:
#     print("数据准确，程序执行正常")

# x = 10
# if x > 5:
#     raise Exception("这是抛出的异常信息")


class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


raise MyException('异常1', '异常2')
