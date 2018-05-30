
list=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]

for i in list:
    for a,b in i.items():
        for c, d in b.items():
            print(a,c,d)


