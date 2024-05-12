#coding=gbk
while 1 :
    n=eval(input('请输入打印行数：'))
    if n%2==0:
        for i in range(0,n//2): #上半个
            if i==0:
                for j in range(0,n//2-1):  #打印空格  
                    print(' ',end="")
                print('*')
            else :
                for j in range(0,n//2-(i+1)):  #打印空格  
                    print(' ',end="")
                print("*",end="")
                for j in range(0,2*i-1):  #打印空格  
                    print(' ',end="")
                print("*")
        for i in range(0,n//2): #下半个
            if i==0:
                print('*',end='')
                for j in range(0,n-3-2*i):
                    print(' ',end='')
                print('*')
            elif i>0 and i< n//2-1:
                for j in range(0,i):
                    print(' ',end='')
                print("*",end='')
                for j in range(0,n-3-2*i):
                    print(' ',end='')
                print("*")
            else :
                for j in range(0,i):
                    print(' ',end='')
                print("*")
    else:
        for i in range(0,n//2): #上半个
            if i==0:
                for j in range(0,n//2):  #打印空格  
                    print(' ',end="")
                print('*')
            else :
                for j in range(0,n//2-(i+1)+1):  #打印空格  
                    print(' ',end="")
                print("*",end="")
                for j in range(0,2*i-1):  #打印空格  
                    print(' ',end="")
                print("*")
                
        print("*",end='') #中间
        for i in range(0,n-2):
            print(" ",end="")
        print("*")        #中间
        
        for i in range(0,n//2): #下半个
            if i==0:
                print(' ',end='')
                print('*',end='')
                for j in range(0,n-4-2*i):
                    print(' ',end='')
                print('*')       #没问题
                
            elif i>0 and i< n//2-1:
                for j in range(0,i+1):
                    print(' ',end='')
                print("*",end='')
                for j in range(0,n-4-2*i):
                    print(' ',end='')
                print("*")
            else :
                for j in range(0,i+1):
                    print(' ',end='')
                print("*")