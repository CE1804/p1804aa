#1. 全局变量
#2. 局部变量

a = 100
def test1():
    print(a)
    c = 1 #函数作用域里边的 遍历为局部变量

def test2():
    print(a)  
    print(c)

#print (c)  #外部 无法访问，函数内容的局部变量

test1()
test2()

