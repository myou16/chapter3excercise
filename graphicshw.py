from graphics import *

def main():
    win=GraphWin()
    shape=Rectangle(Point(20,20),Point(40,40))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p=win.getMouse()
        c=shape.getCenter()
        dx=p.getX()-c.getX()
        dy=p.getY()-c.getY()
        shape.move(dx,dy)

    win.close()

main()

def square():
    win=GraphWin()
    shape=Rectangle(Point(20,20),Point(40,40))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p=win.getMouse()
        p2=Point(p.getX()+20,p.getY()+20)
        new=Rectangle(p,p2)
        new.setOutline("red")
        new.setFill("red")
        new.draw(win)

    Text(Point(100,160),"Click once more to quit").draw(win)
    z=win.getMouse()
    win.close()

square()



def face():
    print("Graphics")
    win=GraphWin("First Graphics Program",600,600)
    Text(Point(100,160),"Click once to draw face").draw(win)
    p1=win.getMouse()
    x=p1.getX()
    y=p1.getY()
    c1=Circle(p1,100)
    c1.setFill('yellow')
    c1.draw(win)
    c2=Circle(Point(x-42,y-30),15)
    c3=Circle(Point(x+42,y-30),15)
    c2.setFill('black')
    c3.setFill('black')
    c2.draw(win)
    c3.draw(win)
    t=Polygon(Point(x,y-15),Point(x-9.5,y+25),Point(x+9.5,y+25))
    t.setFill('green')
    t.draw(win)
    c4=Circle(Point(x-5,y+23),5)
    c5=Circle(Point(x+5,y+23),5)
    c4.setFill('green')
    c4.setOutline('green')
    c5.setFill('green')
    c5.setOutline('green')
    c4.draw(win)
    c5.draw(win)
    mouth=Oval(Point(x-50,y+70),Point(x+50,y+80))
    mouth.setFill('red1')
    mouth.draw(win)
    brim=Rectangle(Point(x-130,y-60),Point(x+130,y-80))
    brim.setFill('blue')
    brim.draw(win)
    hat=Polygon(Point(x,y-250),Point(x-80,y-80),Point(x+80,y-80))
    hat.setFill('blue')
    hat.draw(win)
    

    p=win.getMouse()
    win.close()
                
face()




















