from turtle import *
# for i in range(100):
#     fd(i)
ht()
seth(150)
fillcolor('red')
begin_fill()
for i in range(1,23):
     fd(25)
     rt(i)
up()
home()
down()
seth(30)
end_fill()
begin_fill()
for i in range(1,23):
     fd(25)
     lt(i)
pencolor('red')
home()
end_fill()
mainloop()