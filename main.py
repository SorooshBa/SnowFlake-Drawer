from graphics import *
import random
def findMiddle(a:Point,b:Point):
    c=[]
    c.append((a.x+b.x)/2)
    c.append((a.y+b.y)/2)
    return c
def etoder(win:GraphWin,dotA:Point,dotNot:Point,dots:list):
    dots.remove(dotNot)
    dotB=random.choice(dots)
    dots.append(dotNot)
    t=findMiddle(dotA,dotB)
    p = Point(t[0],t[1])
    p.draw(win)
    return [p,dotB]
x=1
win = GraphWin("snowflake",500*x,500*x)
dot1 = Point(250*x,10*x)
#dot1.draw(win)
dot5 = Point(125*x,100*x)
#dot5.draw(win)
dot2 = Point(375*x,100*x)
#dot2.draw(win)
dot4 = Point(145*x,250*x)
#dot4.draw(win)
dot3 = Point(355*x,250*x)
#dot3.draw(win)

dots = [dot1,dot2,dot3,dot4,dot5]
t=random.choice(dots)
temp=etoder(win,t,t,dots)
for i in range(100000):
    temp=etoder(win,temp[0],temp[1],dots)
win.getMouse()