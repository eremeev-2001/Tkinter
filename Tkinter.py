from tkinter import *
from random  import randrange as rnd, choice
import math


root = Tk()

colors = ('blue', 'lightblue', 'green', 'cyan', 'red', 'purple', 'yellow', 'grey', 'brown')


lf = LabelFrame(root)
lf.pack(side = TOP)
l = Label(lf, text="Очки: 0", font="Arial 32")
l.pack()


canv = Canvas(root, width = 800, height = 600)
canv.pack()

count = 0

'''
Обработчик события нажатия на левую кнопку мыши
'''
def click(event):
    global count
    if event.x > x1 and event.x < x2 and event.y > y1 and event.y < y2:
        count+=1
    l.configure(text = "Очки: " + str(count))

'''
Обработчик события нажатия на клавишу Esc
'''
def escape_click(event):
    root.destroy()    

canv.bind('<Button-1>', click)
root.bind('<Escape>', escape_click)

x = rnd(50, 750)
y = rnd(50, 650)
r = rnd(10,30)
dx = rnd(1,3)
dy = rnd(1,3)
ball = canv.create_oval(x- r, y - r, x + r, y + r, fill = choice(colors))

'''
Перемещение шарика
'''
def ball_move():
    global dx, dy
    
    global x1, y1, x2, y2
    x1 = canv.coords(ball)[0]
    y1 = canv.coords(ball)[1]
    x2 = canv.coords(ball)[2]
    y2 = canv.coords(ball)[3]

    canv.move(ball, dx, dy)      
   
    if x2 >= 800:
        dx = rnd(1,3)*-1
    if x1 <= 0:
        dx = rnd(1,3)    
    if y2 >= 600:
        dy = rnd(1,3)*-1
    if y1 <= r*2:
        dy = rnd(1,3)
    
                                
    root.after(20, ball_move)

ball_move()

root.mainloop()

