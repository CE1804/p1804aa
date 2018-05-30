
#1. 写一个函数
#2. 求三个数的和
#3. 求三个数的平均数

def add(a,b,c):
    return a+b+c

def pingjun(x,y,z):
    s = add(x,y,z)
    return s/3

s = add(1,2,3)
print(s)

p = pingjun(10,10,10)
p = pingjun(1,10,20)
print(p)

'''
#无参 函数
def 函數名称():
     行数执行语句
'''

def print_line():
    print("......")
print_line() #无参函数的使用，调用

# def 函数名（形参）：
def print_user(a):# 一个参数
    print(a)

#print_user('*'*30)

# def 函数名（参数1,参数2）：
def add(a,b):
    print('a+b') # 1.引号引起来的，会原样输出; 
    print(a)  #2.直接写变量，会打印变量保存的数值;

add (1,110)




def question(s):
    print(s)
    xinli ="我才不饿呢。"
    return xinli
r = question("你饿吗？")
print(r)

