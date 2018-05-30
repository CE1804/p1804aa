import random
a=random.randint(1,100)
i = 0
for i in  range(1,11):
    b = int(input("请输入数字"))
    if a > b :
       print("猜小了")
    elif a < b :
       print("猜大了")
    elif a == b :
        print("猜中了")
        break
    i +=1
