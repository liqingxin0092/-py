#coding=gbk
dct={
        'G1569':['�����ϡ������','18:06','18:39','00:33'],
        'G1567':['�����ϡ������','18:06','18:39','00:33'],
        'G1667':['�������������','18:07','18:33','00:13'],
    }
print("����\t����վ������վ\t\t����ʱ��\t����ʱ��\t��ʱ")  
for key,value in dct.items():
    print(key,end='\t')
    for item in value:
        print(item,end='\t\t')
    print()
xuhao=input("������Ҫ��ĳ���>>")
ren=input("������˳��ˣ�����Ƕ������ö��Ÿ���")
flag=0
for key in dct.keys():
    if xuhao ==key:
        if flag==1:
            break;
        flag=1
        print("���ѹ����� ",key,dct.get(key)[0],' ',dct.get(key)[1],'��,','��',ren ,"���컻ȡֽ�ʳ�Ʊ�� ����·�ͷ���",sep='')
if flag==0:
    print("���β�����")