#coding=gbk
while 1 :
    n=eval(input('�������ӡ������'))
    if n%2==0:
        for i in range(0,n//2): #�ϰ��
            if i==0:
                for j in range(0,n//2-1):  #��ӡ�ո�  
                    print(' ',end="")
                print('*')
            else :
                for j in range(0,n//2-(i+1)):  #��ӡ�ո�  
                    print(' ',end="")
                print("*",end="")
                for j in range(0,2*i-1):  #��ӡ�ո�  
                    print(' ',end="")
                print("*")
        for i in range(0,n//2): #�°��
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
        for i in range(0,n//2): #�ϰ��
            if i==0:
                for j in range(0,n//2):  #��ӡ�ո�  
                    print(' ',end="")
                print('*')
            else :
                for j in range(0,n//2-(i+1)+1):  #��ӡ�ո�  
                    print(' ',end="")
                print("*",end="")
                for j in range(0,2*i-1):  #��ӡ�ո�  
                    print(' ',end="")
                print("*")
                
        print("*",end='') #�м�
        for i in range(0,n-2):
            print(" ",end="")
        print("*")        #�м�
        
        for i in range(0,n//2): #�°��
            if i==0:
                print(' ',end='')
                print('*',end='')
                for j in range(0,n-4-2*i):
                    print(' ',end='')
                print('*')       #û����
                
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