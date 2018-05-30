student_list=[] #定义一个空列表
def caidan(): #菜单
    print("欢迎使用「学生信息管理系统」")
    print("*"*40)
    print("1.添加学生信息")
    print("2.显示全部信息")
    print("3.查询学生信息")
    print("4.删除学生信息")
    print("5.修改学生信息")
    print("0.退出系统")
    print("*"*40)
#完成添加一个新信息
def add_new_info():
    name=input("请输入你的姓名：")
    age = input("请输入你的年龄：")
    zhuanye =input("请输入你的专业：")
    phone =input("请输入你的手机号码：")
        
    # 将学生信息保存到一个字典
    info_dict ={'name':name1,'age':age1,'zhuanye':zhuanye1,'phone':phone1}  
    student_list.append(info_dict)
    print(student_list)
        
#显示全部信息
def show_all():
    r = input("请输入查询学生的姓名")
    info_dict["name"] = name
    if r == name:
        print("姓名是%s"% i["name"])
        print("年龄是%s"% i["age"])
        print("专业是%s"% i["zhuanye"])
        print("手机是%s"% i["phone"])
    
#else: 
       # print("没有找到%s"% name)

def find_all_infor():
      global all_infors
      find_name = raw_input("请输入要查找的姓名:")
      find_flag = 0 #默认表示没有找到
      for temp in card_infors:
          if find_name == temp["name"]:
              print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
              find_flag = 1
              break
      if find_flag == 0:
          print("不能找到这个人") 

def update_info(find_dict):
     print(find_name)
     update_name =input("请输入需要修改的名字:"）
     if temp['name'] == mod_name:
         find_dict["name"]=input("请输入新的姓名：")
         find_dict["age"]= input("请输入新的年龄：")
         find_dict["phone"]=input("请输入新的手机号码:")
         print("------修改成功-----")
         return
    print("-------查无此人------")

def delete_info():
    global card_infors
    del_name = raw_input("请输入要删除的姓名:")
    for temp in card_infors:
        if temp['name'] == del_name:
            card_infors.remove(temp)
            break
    print("-------删除完毕--------")

def main():
      #完成对整个模块的调用
    print_menu()
  
    while True:
         #获取用户输入
        num = input("请输入你的选择:")
        if num == 1:
            add_new_card_infor()
        elif num == 2:
            show_all_info()
        elif num == 3:
            find_info()
        elif num == 4:
            update_card_infor()
        elif num == 5:
            delete_info()
        elif num == 0:
             break
        else:             
            print("输入有误,重新输入")
 main() # 主函数执行
