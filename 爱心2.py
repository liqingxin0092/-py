from turtle import *
ht()       #隐藏
title('绘制心形图')   #设置标题
pensize(2)     #调整线的粗细
fillcolor('red')
begin_fill()
seth(45)
fd(200)
circle(100,180)
seth(135)
circle(100,180)
fd(200)
end_fill()
mainloop()