# 定义一个人类
class Person:
    # 设定人类的初始属性
    name = 'default'
    age = 0
    gender = 'male'
    weight = 100

    # 自定义人类的属性，可以通过构造函数init方法传参定义实例的人属性。
    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    @classmethod
    def Play(self):
        print(f"{self.name} playing")

    def Eat(self):
        print(f"{self.name} eating")

    def Study(self):
        print(f"{self.name} study")

    def Sleep(self):
        print(f"{self.name} sleeping")


zs = Person("张三", 20, 'female', 120)
# ls = Person("李四", 25, 'male', 150)
# print(f"姓名：{zs.name}, 年龄：{zs.age}, 性别：{zs.gender}, 体重:{zs.weight}")
# zs.Eat()
# print(f"姓名：{ls.name}, 年龄：{ls.age}, 性别：{ls.gender}, 体重:{ls.weight}")
# ls.Sleep()
# zs.Study()

zs.Eat()
Person.Eat()
