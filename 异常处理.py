try :
    a=int(input("输入被除数:"))
    b=int(input("输入被除数:"))

except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('不能输入字符')
except BaseException:
    print('未知异常')
else:
    result=a/b
    print(result)
finally:
    print('程序执行结束')