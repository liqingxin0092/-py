#coding=gbk
lst =[]
for i in range(2):
    good = input ("������Ʒ�ź���Ʒ>>")
    lst.append(good)
for item in lst:
    print(item)
cart =[]
while 1:
    num=input("��������Ʒ���>>")
    if num=='q':
        break
    for item in lst:
        if item[0:4:]==num:
            cart.append(item)
            print("�ɹ�����",item)
cart.reverse()
for item in cart:
    print("���ﳵ����",item)   

