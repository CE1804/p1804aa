card_infors = [] #定义一个空的列表用来储存名片
def print_menu():
    print("*"*50)
    print("欢迎使用名片管理系统")
    print("1.添加一个名片")
    print("2.删除一个名片")
    print("3.修改一个名片")
    print("4.查询一个名片")
    print("5.显示所有名片")
    print("6.退出管理系统")
    print("*"*50)

def add_card_infor():
    new_name = input("请输入一个名字:")
    new_qq = input("请输入QQ号:")
    new_phone = input("请输入手机号:")
    new_addr = input("请输入地址:")
    #定义一个新的字典，用来储存一个新的名片
    new_infor = {}
    new_infor["name"] = new_name
    new_infor["qq"] = new_qq
    new_infor["phone"] = new_phone
    new_infor["addr"] = new_addr
    
    #将字典添加到列表中
    card_infors.append(new_infor)
    #print(card_infors) #for test

def dele_card_infor():
    dele_name = input("请输入要删除的姓名:")
    find_flag = 0 #默认表示没有找到
    for temp in card_infors:
        if dele_name==temp["name"]:
            find_flag = 1 #表示找到了   
            card_infors.remove(temp)
            print("删除成功！")  
            break
    if find_flag==0:
        print("查无此人!")

def update_card_infor():
    update_name = input("请输入要修改的人的姓名：")   #输入要修改的姓名
    find_flag = 0                                 #默认表示没有找到
    update_flag = 0                               #默认修改失败
    sign = 0
    for temp in card_infors:
        sign+=1
        if update_name==temp["name"]:
            find_flag = 1
            print("1.修改姓名")                    #打印修改菜单
            print("2.修改QQ")
            print("3.修改微信")
            print("4.修改地址")
            print("5.退出修改")
            while True:
                num2 = int(input("请输入要修改信息的编号：")) 
                if num2==1:
                    card_infors[sign-1]["name"] = input("请输入您要修改后的姓名:")  
                    update_flag = 1
                elif num2==2:
                    card_infors[sign-1]["qq"] = int(input("请输入您要修改后的QQ:"))
                    update_flag = 1
                elif num2==3:
                    card_infors[sign-1]["phone"] = input("请输入您修改后的手机号:")
                    update_flag = 1
                elif num2==4:
                    card_infors[sign-1]["addr"] = input("请输入您要修改后的地址:")
                    update_flag = 1
                elif num2==5:
                    break
                else:
                    print("输入有误，请重新输入:")
                if update_flag==1:                
                    print("修改成功！")
                print("")
            break
    if find_flag==0:
        print("查无此人！")

def find_card_infor():
    find_name = input("请输入你要查找的姓名:")
    find_flag = 0 #默认表示没有找到
    for temp in card_infors:
        if find_name==temp["name"]:
            print("%s\t%s\t%s\t%s"%(temp["name"], temp["qq"], temp["phone"], temp["addr"]))
            find_flag = 1 #表示找到了
            break
    if find_flag==0:
        print("查无此人!")


def show_card_infor():
    print("姓名\tQQ\t微信\t地址")
    for temp in card_infors:
        print("%s\t%s\t%s\t%s"%(temp["name"], temp["qq"], temp["phone"], temp["addr"]))

def main():
    while True:
        print_menu()
        num = int(input("请输入功能序号:"))  #获取用户的选择
        
        #根据用户的选择执行相应的功能
        if num==1:
            add_card_infor()
        elif num==2:
            dele_card_infor()
        elif num==3:
            update_card_infor()
        elif num==4:
            find_card_infor()
        elif num==5:
            show_card_infor()
        elif num==6:
            break
        else:
            print("你的输入有误，请重新输入！")
        print("")

main() #调用主函数
