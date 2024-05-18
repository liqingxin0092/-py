lst=[
    ['01',"洗衣机",'美的',500],
    ['02',"电饭煲",'美的',500],
    ['03',"电风扇",'海尔',500],
]
print("编号\t\t物品\t\t厂商\t\t价格")
# for item in lst:
#     for i in item:
#         print(i,end='  \t')
#     print()
for item in lst:
    item[0]='000'+item[0]
    item[3]=f'${item[3]}'

for item in lst:
    for i in item:
        print(i,end='  \t')
    print()