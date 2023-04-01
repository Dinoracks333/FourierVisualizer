import pygame as pg
import math
from rotateReal import rRotate
class vector:
  def __init__(self,constant,frequency,x,y,length):
    self.c=constant
    self.f=frequency
    self.x=x
    self.y=y
    self.tipx=x+5
    self.tipy=y
    self.l=length
    self.w=length/4
  def rotate(self,val):
    self.r+=val
  def setPos(self,x,y):
    self.x=x
    self.y=y
pg.init()
#fin=open("star.in","r") #60
#fin=open("arr.out","r") #60
#fin=open("rj.out","r") #1000
fin=open("alex.out","r") #500
#fin=open("RJLogoVals.out","r") #500
#fin=open("dang.out","r") #500
n=int(fin.readline())
a,b=[float(x) for x in fin.readline().split()]
arrows=[vector(b-math.pi/2,0,0,0,a)]
prev=(0,0)
for i in range(2,n+2):
  a,b=[float(x) for x in fin.readline().split()]
  arrows.append(vector(b-math.pi/2,i//2*(i%2*2-1),0,0,a))
lines=[]
check=True
screen = pg.display.set_mode((700, 700))
clock = pg.time.Clock()
image=pg.image.load("arrow.png")
arrowt=pg.transform.rotate(image,90)
arrowt=pg.transform.scale(arrowt,(10,40))
x=0
while(True):
  for event in pg.event.get() :
        if event.type == pg.QUIT :
            pg.quit()
            quit()
  screen.fill((0,0,0))
  last=(0,0)
  for arrow in arrows: #go through the arrows and update positions from parent to child
    arrow.x,arrow.y=last
    temp=pg.transform.scale(arrowt,(arrow.w,arrow.l))
    if(arrow!=arrows[0]):
      screen.blit(pg.transform.rotate(temp,x*arrow.f+arrow.c*180/math.pi),rRotate(arrow.x,arrow.y,arrow.w,arrow.l,x*arrow.f+arrow.c*180/math.pi,2))
    arrow.tipx,arrow.tipy=arrow.x-arrow.l*math.sin(x*arrow.f*math.pi/180 +arrow.c),arrow.y-arrow.l*math.cos(x*arrow.f*math.pi/180+arrow.c)
    last=(arrow.tipx,arrow.tipy)
  if(check):
    if(x==0):
      prev=last
    lines.append((prev,last))
    prev=list(last)
  for item in lines: #draw the lines from the arrows
    pg.draw.line(screen,(255,255,255),item[0],item[1])
  pg.display.flip()
  clock.tick(60)
  x=(x+1)%360
  if(check and x==0):
    check=False
