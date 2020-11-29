from hogwarts_study import random

computer_number = random.randint(1, 101)

while True:

    person_number = int(input("请输入一个数字："))

    if person_number > computer_number:
        print("小一点")
        continue

    elif person_number < computer_number:
        print("大一点")
        continue
    else:
        print("猜对了：数字为%d" %(computer_number))
    break
