#coding=gbk
lst =[]
for i in range(2):
    good = input ("输入商品号和商品>>")
    lst.append(good)
for item in lst:
    print(item)
cart =[]
while 1:
    num=input("请输入商品编号>>")
    if num=='q':
        break
    for item in lst:
        if item[0:4:]==num:
            cart.append(item)
            print("成功导入",item)
cart.reverse()
for item in cart:
    print("购物车里有",item)   

