from tkinter import *
from Wall import Wall
from Obstacle import Obstacle
from Player import Player
from Wallpad import Wallpad
import random

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

class Step_move:
    def __init__(self,parent):
        self.parent = parent
        self.canvas = Canvas(self.parent,width=DISPLAY_WIDTH,height=DISPLAY_HEIGHT,bg = 'white')
        self.canvas.pack()

#user story
#เพื่อที่จะตรวจสอบการชนของผู้เล่นกับกล่อง
#ฉันเป็นผู้สร้าง
#ต้องการรู้ว่าผู้เล่นชนกับกล่องหรือไม่

#scenario:
#ให้ผู้เล่นชนกับกล่อง
#เมื่อตรวจสอบแล้ว
#จึงแสดงว่าผู้เล่นชนกับกล่องหรือไม่

#purpose:ตรวจสอบการชนของผู้เล่นกับกล่อง
#input:กล่อง(int),ผู้เล่น(int)
#output:ชนหรือไม่ชน(boolean)
#contract:hitplayer(int,int)-->(boolean)
#example:hitplayer(Mobstacle,mplayer)-->True
#        hitplayer(Mobstacle,mplayer)-->False
        
    def hitPlayer(self,Mobstacle,mplayer):
        xP1,yP1,xP2,yP2 = self.getCurPos(mplayer)
        xa1,ya1,xa2,ya2, = self.getCurPos(Mobstacle)
        if xP1 <= xa2 and xP2 >= xa1 and yP1 <= ya2-12 and yP2 >= ya1+3 :
            return True
        else: return False

#user story
#เพื่อที่จะสร้างกรอบหน้าจอ
#ฉันเป็นผู้ออกแบบ
#ต้องการสร้างกรอบหน้าจอ

#scenario:
#ให้เส้นตารางแสดงบนล่างซ้ายและขวา
#เมื่อทำการสร้าง
#จึงแสดงเส้นกรอบ

#purpose:สร้างกรอบหน้าจอ
#input:จุดที่จะสร้าง(int)
#output:เส้นกรอบ(Nonetype)
#contract:createtable(int)-->(Nonetype)
#example:createtable(aWall)-->เส้นกรอบ
        
    def createtable(self,aWall):
        leftWall=self.canvas.create_line(aWall.xLeft,aWall.xTop,aWall.xLeft,aWall.xBottom)
        RightWall=self.canvas.create_line(aWall.xRight,aWall.xTop,aWall.xRight,aWall.xBottom)
        TopWall=self.canvas.create_line(aWall.xLeft,aWall.xTop,aWall.xRight,aWall.xTop)
        BottomWall=self.canvas.create_line(aWall.xLeft,aWall.xBottom,aWall.xRight,aWall.xBottom)
        
#user story
#เพื่อที่จะสร้างช่องสี่เหลี่ยม
#ฉันเป็นผู้ออกแบบ
#ต้องการสร้างช่องสี่เหลี่ยม

#scenario:
#ให้ช่องสี่เหลี่ยมแสดงตรงกลาง
#เมื่อทำการสร้าง
#จึงแสดงช่องสี่เหลี่ยม
        
#purpose:สร้างช่องสี่เหลี่ยม
#input:จุดที่จะสร้าง(int),สี(str)
#output:ช่องสี่เหลี่ยม(Nonetype)
#contract:createWallpad(int,str)-->(Nonetype)
#example:createWallpad(aWallpad,color)-->ช่องสีเหลี่ยม
        
    def createWallpad(self,aWallpad,color):
        x1 = aWallpad.x1
        y1 = aWallpad.y1
        x2 = aWallpad.x2
        y2 = aWallpad.y2
        self.canvas.create_rectangle(x1,y1,x2,y2,fill=color)

#user story
#เพื่อที่จะสร้างตัวละครของผู้เล่น
#ฉันเป็นผู้ออกแบบ
#ต้องการสร้างรูปตัวละคร

#scenario:
#ให้ตัวละครแสดงบนหน้าจอ
#เมื่อทำการสร้าง
#จึงแสดงตัวละคร
        
#purpose:สร้างตัวละครของผู้เล่น
#input:จุดที่จะสร้าง(int),รูป(tkinter.PhotoImage)
#output:แสดงรูปตัวละคร(type)
#contract:createPlayer(int,tkinter.PhotoImage)-->(type)
#example:createPlayer(aPlay,image)-->รูปตัวละคร

    def createPlayer(self,aPlay,image):
        x1 = aPlay.xpos
        y1 = aPlay.ypos
        img = image
        Player = self.canvas.create_image(aPlay.xpos,aPlay.ypos,image = image)
        return Player

#user story
#เพื่อที่จะเคลื่อนย้ายและตรวจสอบตำแหน่งของตัวละครผู้เล่น
#ฉันเป็นผู้ออกแบบ
#ต้องการเคลื่อนย้ายและตรวจสอบตำแหน่งตัวละครผู้เล่น

#scenario1:
#ให้ตรวจสอบการเคลื่อนย้ายตัวละครไปยังจุดที่จะทำให้ชนะ
#เมื่อทำการตรวจสอบการเคลื่อนย้ายไปยังจุดที่ชนะ
#จึงจะแสดง"You Win!"

#scenario2:
#ให้ตรวจสอบการเคลื่อนย้ายตัวละครไปชนเส้นกรอบ
#เมื่อทำการตรวจสอบการเคลื่อนย้ายไปชนเส้นกรอบ
#จึงจะแสดง"Game Over!"

#scenario3:
#ให้ตรวจสอบการเคลื่อนย้ายตัวละครไปชนกล่อง
#เมื่อทำการตรวจสอบการเคลื่อนย้ายไปชนกล่อง
#จึงหยุดทุกอย่างและแสดง"Game Over!"
        
#purpose:ต้องการเคลื่อนย้ายและตรวจสอบตำแหน่งตัวละครผู้เล่น
#input:ความเร็วแนวราบ(int),ความเร็วแนวดิ่ง(int),ตัวละคร(int)
#output:แสดงข้อความ'You Win!'หรือ'Game Over!'(tkinter.text)
#contract:movePlayer(int,int,int)-->(tkinter.text)
#example:movePlayer(xSpeed,ySpeed,mplayer)-->You Win!
#        movePlayer(xSpeed,ySpeed,mplayer)-->Game Over!

    def movePlayer(self,xSpeed,ySpeed,mplayer):
        self.canvas.move(mplayer,xSpeed,0)
        self.canvas.move(mplayer,0,ySpeed)
        if self.Win(aWall,mplayer)== True:
            root=Tk()
            gamewin = Label(root,font=('arial',25,'bold'),text='You Win!', fg='white',anchor='center',bd=300,bg='green',width=10,height = 2)
            gamewin.pack()
            root.mainloop()
        if self.hitWallPlayer(aWall,mplayer) == True:
            aPlay.vel = 0
            root=Tk()
            gameover = Label(root,font=('arial',25,'bold'),text='Game Over!', fg='white',anchor='center',bd=300,bg='red',width=10,height = 2)
            gameover.pack()
            root.mainloop()
        if self.hitPlayer(Mobstacle,mplayer) == True:
            aPlay.vel = 0
            aobstacle.xvel = 0
            root=Tk()
            gameover = Label(root,font=('arial',25,'bold'),text='Game Over!', fg='white',anchor='center',bd=300,bg='red',width=10,height = 2)
            gameover.pack()
            root.mainloop()

#user story
#เพื่อที่จะเคลื่อนย้ายตำแหน่งของตัวละครผู้เล่น
#ฉันเป็นผู้ออกแบบ
#ต้องการเคลื่อนย้ายตำแหน่งตัวละครผู้เล่น

#scenario1:
#ให้กดปุ่มไปทางด้านซ้าย
#เมื่อทำการตรวจสอบการเคลื่อนที่ของปุ่มที่กด
#จึงจะแสดงการเคลื่อนย้ายตัวละครไปทางด้านซ้าย

#scenario2:
#ให้กดปุ่มไปทางด้านขวา
#เมื่อทำการตรวจสอบการเคลื่อนที่ของปุ่มที่กด
#จึงจะแสดงการเคลื่อนย้ายตัวละครไปทางด้านขวา

#scenario3:
#ให้กดปุ่มไปทางด้านบน
#เมื่อทำการตรวจสอบการเคลื่อนที่ของปุ่มที่กด
#จึงจะแสดงการเคลื่อนย้ายตัวละครไปทางด้านบน

#scenario4:
#ให้กดปุ่มไปทางด้านล่าง
#เมื่อทำการตรวจสอบการเคลื่อนที่ของปุ่มที่กด
#จึงจะแสดงการเคลื่อนย้ายตัวละครไปทางด้านล่าง
        
#purpose:ต้องการเคลื่อนย้ายตัวละครผู้เล่น
#input:ความเร็ว(int),ตัวละคร(int)
#output:เปลี่ยนตำแหน่งของตัวละคร
#contract:controlPlayer(int,int)-->(int)
#example:controlPlayer(aPlay,mplayer)-->เปลี่ยนตำแหน่งตัวละครไปทางซ้าย
#        controlPlayer(aPlay,mplayer)-->เปลี่ยนตำแหน่งตัวละครไปทางขวา
#        controlPlayer(aPlay,mplayer)-->เปลี่ยนตำแหน่งตัวละครไปทางบน
#        controlPlayer(aPlay,mplayer)-->เปลี่ยนตำแหน่งตัวละครไปทางล่าง
            
    def controlPlayer(self,aPlay,mplayer):
        self.parent.bind("<KeyPress-Left>",lambda Left:self.movePlayer(-aPlay.vel,0,mplayer))
        self.parent.bind("<KeyPress-Right>",lambda Right:self.movePlayer(aPlay.vel,0,mplayer))
        self.parent.bind("<KeyPress-Up>",lambda Up:self.movePlayer(0,-aPlay.vel,mplayer))
        #self.parent.bind("<KeyPress-Down>",lambda Down:self.movePlayer(0,aPlay.vel,mplayer))

#user story
#เพื่อที่จะสร้างกล่องสี่เหลี่ยม
#ฉันเป็นผู้ออกแบบ
#ต้องสร้างกล่องสี่เหลี่ยม

#scenario1:
#ให้กล่องสี่เหลี่ยมแสดงบนหน้าจอ
#เมื่อทำการสร้าง
#จึงแสดงกล่องสี่เหลี่ยม

#purpose:ต้องการสร้างสี่เหลี่ยม
#input:จุดที่ต้องการให้แสดง(int),สี(str)
#output:แสดงกล่องสี่เหลี่ยม(None)
#contract:createobstacle(int,str)-->(int)
#example:createobstacle(aobstacle,color)-->กล่องสี่เหลี่ยม

    def createobstacle(self,aobstacle,color):
        x1 = aobstacle.xpos
        y1 = aobstacle.ypos
        x2 = aobstacle.xpos + aobstacle.width
        y2 = aobstacle.ypos + aobstacle.height
        obstacle = self.canvas.create_rectangle(x1,y1,x2,y2,fill=color)
        return obstacle

#user story
#เพื่อที่จะเคลื่อนย้ายและตรวจสอบการชนของกล่องสี่เหลี่ยม
#ฉันเป็นผู้ออกแบบ
#ต้องเคลื่อนย้ายและตรวจสองการชนของกล่องสี่เหลี่ยม

#scenario1:
#ให้ตรวจสอบการเคลื่อนย้ายกล่องสี่เหลี่ยมไปชนกรอบ
#เมื่อทำการตรวจสอบการเคลื่อนย้ายกล่องไปชนกรอบ
#จึงเปลี่ยนทิศทางการเคลื่อนที่ของกล่องสี่เหลี่ยม

#scenario2:
#ให้ตรวจสอบการเคลื่อนย้ายกล่องสี่เหลี่ยมไปชนตัวละคร
#เมื่อทำการตรวจสอบการเคลื่อนย้ายกล่องไปชนกับตัวละครผู้เล่น
#จึงจะหยุดเกมและแสดง"Game Over"


#purpose:ต้องการเคลื่อนย้ายกล่องสี่เหลี่ยม
#input:กล่อง(int),จุดที่ต้องการให้แสดง(int)
#output:เปลี่ยนทิศการเคลื่อนที่(int) หรือ Game Over!(tkinter.text)
#contract:moveobstacle(int,tkinter.text)-->(int)
#example:moveobstacle(Mobstacle,aobstacle)-->เปลี่ยนทิศทางการเคลื่อนที่
#        moveobstacle(Mobstacle,aobstacle)-->Game Over!

    def moveobstacle(self,Mobstacle,aobstacle):
        self.canvas.move(Mobstacle,aobstacle.xvel,aobstacle.yvel)
        if self.hitWallObstacle(aWall,Mobstacle,aobstacle) == True:
            aobstacle.xvel = - aobstacle.xvel
        if self.hitPlayer(Mobstacle,mplayer) == True:
            aPlay.vel = 0
            aobstacle0.xvel = 0
            aobstacle1.xvel = 0
            aobstacle2.xvel = 0
            aobstacle3.xvel = 0
            aobstacle4.xvel = 0
            aobstacle5.xvel = 0
            aobstacle6.xvel = 0
            aobstacle7.xvel = 0
            aobstacle8.xvel = 0
            aobstacle9.xvel = 0
            root=Tk()
            gameover = Label(root,font=('arial',25,'bold'),text='Game Over!', fg='white',anchor='center',bd=300,bg='red',width=10,height = 2)
            gameover.pack()
            root.mainloop()
        self.canvas.after(10,self.moveobstacle,Mobstacle,aobstacle)

    def getCurPos(self,obj):
        return self.canvas.bbox(obj)

#user story
#เพื่อที่จะจบเกมโดยชนะ
#ฉันเป็นผู้เล่น
#ต้องเคลื่อนย้ายตัวละครไปยังกรอบด้านบน

#scenario1:
#ให้ตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่ที่กรอบด้านบน
#เมื่อทำการตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่กรอบด้านบน
#จึง return True

#scenario2:
#ให้ตรวจสอบการเคลื่อนย้ายตัวละครว่าไม่อยู่ที่กรอบด้านบน
#เมื่อทำการตรวจสอบการเคลื่อนย้ายตัวละครว่าไม่อยู่กรอบด้านบน
#จึง return False

#purpose:ต้องการตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่กรอบด้านบนหรือไม่
#input:กรอบ(int),ตัวละครผู้เล่น(int)
#output:True or False(boolean)
#contract:Win(int,int)-->(boolean)
#example:Win(aWall,mplayer)-->True
#        Win(aWall,mplayer)-->False
    
    def Win(self,aWall,mplayer):
        xa1,ya1,xa2,ya2 = self.getCurPos(mplayer)
        if ya1 <= aWall.xTop-10:
            return True
        else:
            return False

#user story
#เพื่อที่จะ game over
#ฉันเป็นผู้เล่น
#ต้องเคลื่อนที่ไปชนกับ

#scenario1:
#ให้ตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่ที่กรอบด้านซ้าย
#เมื่อทำการตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่กรอบด้านซ้าย
#จึง return True

#scenario2:
#ให้ตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่ที่กรอบด้านขวา
#เมื่อทำการตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่กรอบด้านขวา
#จึง return True

#scenario3:
#ให้ตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่ที่กรอบด้านล่าง
#เมื่อทำการตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่กรอบด้านล่าง
#จึง return True

#scenario4:
#ให้ตรวจสอบการเคลื่อนย้ายตัวละครว่าไม่อยู่ที่กรอบ
#เมื่อทำการตรวจสอบการเคลื่อนย้ายตัวละครว่าไม่อยู่ที่กรอบ
#จึง return False

#purpose:ต้องการตรวจสอบการเคลื่อนย้ายตัวละครว่าอยู่กรอบด้านบนหรือไม่
#input:กรอบ(int),ตัวละครผู้เล่น(int)
#output:True or False(boolean)
#contract:Win(int,int)-->(boolean)
#example:Win(aWall,mplayer)-->True
#        Win(aWall,mplayer)-->False

    def hitWallPlayer(self,aWall,mplayer):
        x1,y1,x2,y2 = self.getCurPos(mplayer)
        if aWall.xLeft >= x1:
            return True
        if aWall.xRight <= x2:
            return True
        if aWall.xBottom+10 <= y2:
            return True
        else:
            return False

#user story
#เพื่อที่จะตรวจสอบว่ากล่องชนกรอบหรือไม่
#ฉันเป็นผู้ออกแบบ
#ต้องตรวจสอบว่ากล่องชนกรอบหรือไม่

#scenario1:
#ให้ตรวจสอบการเคลื่อนย้ายกล่องว่าอยู่ที่กรอบด้านซ้าย
#เมื่อทำการตรวจสอบการเคลื่อนย้ายกล่องว่าอยู่กรอบด้านซ้าย
#จึง return True

#scenario2:
#ให้ตรวจสอบการเคลื่อนย้ายกล่องว่าอยู่ที่กรอบด้านขวา
#เมื่อทำการตรวจสอบการเคลื่อนย้ายกล่องว่าอยู่กรอบด้านขวา
#จึง return True
        
#scenario4:
#ให้ตรวจสอบการเคลื่อนย้ายกล่องว่าไม่อยู่ที่กรอบด้านซ้ายหรือขวา
#เมื่อทำการตรวจสอบการเคลื่อนย้ายกล่องว่าไม่อยู่ที่กรอบ
#จึง return False

#purpose:ต้องการตรวจสอบการเคลื่อนย้ายกล่องว่าอยู่กรอบด้านซ้ายหรือขวาหรือไม่
#input:กรอบ(int),กล่อง(int)
#output:True or False(boolean)
#contract:hitWallObstacle(int,int,int)-->(boolean)
#example:hitWallObstacle(aWall,mplayer)-->True
#        hitWallObstacle(aWall,mplayer)-->False

    def hitWallObstacle(self,aWall,Mobstacle,aobstacle):
        x1,y1,x2,y2 = self.getCurPos(Mobstacle)
        if aobstacle.xvel < 0 and aWall.xLeft >= x1 + aobstacle.width + 20:
            return True
        if aobstacle.xvel > 0 and aWall.xRight <= x2 - aobstacle.width - 20:
            return True
        else:
            return False

    

x = range(0,800)
xpose = random.choice(x)
xpose1 = random.choice(x)
xpose2 = random.choice(x)
xpose3 = random.choice(x)
xpose4 = random.choice(x)
xpose5 = random.choice(x)
xpose6 = random.choice(x)
xpose7 = random.choice(x)
xpose8 = random.choice(x)
xpose9 = random.choice(x)
            
      
root = Tk()
root.title("Step move")
#add widgets
myApp = Step_move(root)
#===================================================================

#Wall
aWall = Wall(3,800,3,600)
myApp.createtable(aWall)

bWallpad = Wallpad(3,550,800,600)
myApp.createWallpad(bWallpad,"light green")

cWallpad = Wallpad(3,3,100,25)
myApp.createWallpad(cWallpad,"black")

cWallpad = Wallpad(100,25,200,50)
myApp.createWallpad(cWallpad,"black")

cWallpad = Wallpad(200,3,300,25)
myApp.createWallpad(cWallpad,"black")

cWallpad = Wallpad(300,25,400,50)
myApp.createWallpad(cWallpad,"black")

cWallpad = Wallpad(400,3,500,25)
myApp.createWallpad(cWallpad,"black")

cWallpad = Wallpad(500,25,600,50)
myApp.createWallpad(cWallpad,"black")

cWallpad = Wallpad(600,3,700,25)
myApp.createWallpad(cWallpad,"black")

cWallpad = Wallpad(700,25,800,50)
myApp.createWallpad(cWallpad,"black")

dWallpad = Wallpad(3,50,800,100)
myApp.createWallpad(dWallpad,"#DCDCDC")
dWallpad = Wallpad(3,100,800,150)
myApp.createWallpad(dWallpad,"#FFFFF0")
dWallpad = Wallpad(3,150,800,200)
myApp.createWallpad(dWallpad,"#DCDCDC")
dWallpad = Wallpad(3,200,800,250)
myApp.createWallpad(dWallpad,"#FFFFF0")
dWallpad = Wallpad(3,250,800,300)
myApp.createWallpad(dWallpad,"#DCDCDC")
dWallpad = Wallpad(3,300,800,350)
myApp.createWallpad(dWallpad,"#FFFFF0")
dWallpad = Wallpad(3,350,800,400)
myApp.createWallpad(dWallpad,"#DCDCDC")
dWallpad = Wallpad(3,400,800,450)
myApp.createWallpad(dWallpad,"#FFFFF0")
dWallpad = Wallpad(3,450,800,500)
myApp.createWallpad(dWallpad,"#DCDCDC")
dWallpad = Wallpad(3,500,800,550)
myApp.createWallpad(dWallpad,"#FFFFF0")

imgPl = PhotoImage(file='Playerimg.png')
aPlay = Player(400,570,50)
mplayer = myApp.createPlayer(aPlay,imgPl)

#=========================================================================
#Obstacle
aobstacle0 = Obstacle(xpose,50,7.5,0)
Mobstacle0 = myApp.createobstacle(aobstacle0,"orange")
myApp.moveobstacle(Mobstacle0,aobstacle0)

aobstacle1 = Obstacle(xpose1,100,7,0)
Mobstacle1 = myApp.createobstacle(aobstacle1,"green")
myApp.moveobstacle(Mobstacle1,aobstacle1)

aobstacle2 = Obstacle(xpose2,150,6.5,0)
Mobstacle2 = myApp.createobstacle(aobstacle2,"pink")
myApp.moveobstacle(Mobstacle2,aobstacle2)
    
aobstacle3 = Obstacle(xpose3,200,6,0)
Mobstacle3 = myApp.createobstacle(aobstacle3,"red")
myApp.moveobstacle(Mobstacle3,aobstacle3)

aobstacle4 = Obstacle(xpose4,250,5.5,0)
Mobstacle4 = myApp.createobstacle(aobstacle4,"blue")
myApp.moveobstacle(Mobstacle4,aobstacle4)

aobstacle5 = Obstacle(xpose5,300,5,0)
Mobstacle5 = myApp.createobstacle(aobstacle5,"brown")
myApp.moveobstacle(Mobstacle5,aobstacle5)

aobstacle6 = Obstacle(xpose6,350,4.5,0)
Mobstacle6 = myApp.createobstacle(aobstacle6,"yellow")
myApp.moveobstacle(Mobstacle6,aobstacle6)

aobstacle7 = Obstacle(xpose7,400,4,0)
Mobstacle7 = myApp.createobstacle(aobstacle7,"grey")
myApp.moveobstacle(Mobstacle7,aobstacle7)

aobstacle8 = Obstacle(xpose8,450,3.5,0)
Mobstacle8 = myApp.createobstacle(aobstacle8,"gold")
myApp.moveobstacle(Mobstacle8,aobstacle8)

aobstacle9 = Obstacle(xpose9,500,3,0)
Mobstacle9 = myApp.createobstacle(aobstacle9,"light blue")
myApp.moveobstacle(Mobstacle9,aobstacle9)


#===============================================================
#Player

myApp.controlPlayer(aPlay,mplayer)
#===============================================================

root.mainloop()
