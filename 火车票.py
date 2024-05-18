#coding=gbk
dct={
        'G1569':['北京南—天津南','18:06','18:39','00:33'],
        'G1567':['北京南—天津南','18:06','18:39','00:33'],
        'G1667':['北京西—天津南','18:07','18:33','00:13'],
    }
print("车次\t出发站—到达站\t\t出发时间\t到达时间\t历时")  
for key,value in dct.items():
    print(key,end='\t')
    for item in value:
        print(item,end='\t\t')
    print()
xuhao=input("请输入要买的车次>>")
ren=input("请输入乘车人，如果是多人请用逗号隔开")
flag=0
for key in dct.keys():
    if xuhao ==key:
        if flag==1:
            break;
        flag=1
        print("您已购买了 ",key,dct.get(key)[0],' ',dct.get(key)[1],'开,','请',ren ,"尽快换取纸质车票。 【铁路客服】",sep='')
if flag==0:
    print("车次不存在")