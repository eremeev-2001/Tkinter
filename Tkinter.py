
from tkinter import *
from random  import randrange as rnd, choice

print("Напишите Ваше имя:")
name=input()

width = 1000
height = 500

colors = ('blue', 'lightblue', 'green', 'cyan', 'red', 'purple', 'yellow', 'grey', 'brown', 'aqua', 'fuchsia', 'maroon', 'pink', 'purple', 'violet')

root = Tk()
lf = LabelFrame(root)
lf.pack(side = TOP)
l = Label(lf, text="Очки: 0", font="Arial 32")
l.pack()

canv = Canvas(root, width=width, height=height )
canv.pack()

count = 0
ball_list = []
rhomb_list = []

'''
Обработчик события нажатия на левую кнопку мыши
'''
def click(event):
    global count, ball_list, rhomb_list
    for obj in ball_list:
        if event.x > canv.coords(obj)[0] and event.x < canv.coords(obj)[2] and event.y > canv.coords(obj)[1] and event.y < canv.coords(obj)[3]:
            count+=2
            
    for obj in rhomb_list:
        if event.x >= canv.coords(obj)[0] and event.x < canv.coords(obj)[4] and event.y > canv.coords(obj)[3] and event.y < canv.coords(obj)[7]:
            count+=1
            
    l.configure(text = "Очки: " + str(count))                        

'''
Обработчик события нажатия на клавишу Esc
'''
def escape_click(event):
    root.destroy()    

canv.bind('<Button-1>',click)
root.bind('<Escape>', escape_click)

class Ball:
    def __init__(self, ball_list):        
        self.x = rnd(50, 750)
        self.y = rnd(50, 650)
        self.r = rnd(10,30)
        self.dx = rnd(1,3)
        self.dy = rnd(1,3)
        
        self.ball = canv.create_oval(self.x- self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = choice(colors))
       
        ball_list.append(self.ball)
        self.ball_move()

    def ball_move(self):                
        x1, y1, x2, y2 = canv.coords(self.ball)
        canv.move(self.ball, self.dx, self.dy)      
   
        if x2 >=width :
            self.dx = rnd(1,3)*-1
        if x1 <= 0:
            self.dx = rnd(1,3)    
        if y2 >=height :
            self.dy = rnd(1,3)*-1
        if y1 <= self.r*2:
            self.dy = rnd(1,3)
                                
        root.after(20, self.ball_move)

class Rhomb:
    def __init__(self, rhomb_list):        
        self.x = rnd(50, 750)
        self.y = rnd(50, 650)
        self.r = rnd(10,30)
        self.dx = rnd(1,3)
        self.dy = rnd(1,3)
        
        self.rhomb = canv.create_polygon((self.x - self.r, self.y), (self.x, self.y - self.r), (self.x + self.r, self.y), (self.x, self.y + self.r),
            fill = choice(colors))
       
        rhomb_list.append(self.rhomb)
        self.rhomb_move()

    def rhomb_move(self):                
        x1, y1, x2, y2, x3, y3, x4, y4 = canv.coords(self.rhomb)
        canv.move(self.rhomb, self.dx, self.dy)      
   
        if x3 >= width:
            self.dx = rnd(1,3)*-1
        if x1 <= 0:
            self.dx = rnd(1,3)    
        if y4 >= height:
            self.dy = rnd(1,3)*-1
        if y2 <= self.r*2:
            self.dy = rnd(1,3)
                                
        root.after(20, self.rhomb_move)             
            

Ball(ball_list)
Ball(ball_list)
Ball(ball_list)
Ball(ball_list)
Ball(ball_list)

Rhomb(rhomb_list)
Rhomb(rhomb_list)
Rhomb(rhomb_list)
Rhomb(rhomb_list)
Rhomb(rhomb_list)

root.mainloop()


f = open('Результаты игр.txt', 'a')
f.write(name +" "+str(count)+"\n")
f.close()

