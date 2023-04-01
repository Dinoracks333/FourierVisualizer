"""
NOTES ON FUNCTIONALITY:
left click to add a dot
right click to remove previous dot
Dots will auto adjust to spots of contrast near where you clicked, so you don't have to be super precise in clicking for the outline
Pressing enter will complete the outline, filling in gaps between dots that you entered in and will save the resulting data points into the file name that you specify
The file that you generate can be put directly into getVals.py to create a file containing
all of the relevant information to draw the image (so you can just open it in the main program)
"""


import pygame as pg
pg.init()
fout=open("alexpic.out","w") #specify output file name here
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
image=pg.image.load("alexMe.jpeg")
ratio=image.get_width()/image.get_height()
ratio=min(ratio,1/ratio)
if(image.get_width()<image.get_height()):
  image=pg.transform.scale(image,(400*ratio,400))
else:
  image=pg.transform.scale(image,(400,400*ratio))
spots=[]
def inside(x,y):
  return x<500 and x>=0 and y<500 and y>=0
def check(c1,c2):
  tot=0
  for i in range(3):
    tot+=abs(c1[i]-c2[i])/255
  return tot>=.6
def findContrast(start,color,visited=set()):
  q=[list(start)]
  for i in range(400): #limit to 20x20 grid BFS
    s=q.pop(0)
    key=500*s[1]+s[0]
    if(key in visited or not inside(s[0],s[1])):
      continue
    col=screen.get_at(s)
    if(check(color,col)):
      return s
    visited.add(key)
    for j in range(-1,2):
      for k in range(-1,2):
        a,b=s[0]+j,s[1]+k
        if(b*500+a in visited or not inside(a,b)):
          continue
        q.append([a,b])
  return start
running=True
while(running):
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      pg.quit()
      quit()
    elif(event.type==pg.MOUSEBUTTONDOWN):
      if(pg.mouse.get_pressed()[2]):
        if(len(spots)==0):
          continue
        spots.pop(-1)
      else:
        start=pg.mouse.get_pos()
        color=screen.get_at(start)
        spot=findContrast(start,color,set())
        spots.append(spot)
    elif(event.type==pg.KEYDOWN):
      if(event.key==pg.K_RETURN):
        pg.quit()
        running=False
        for i in range(len(spots)):
          fout.write(str(spots[i][0])+" "+str(spots[i][1])+"\n")
          xchange,ychange=spots[i][0]-spots[i-1][0],spots[i][1]-spots[i-1][1]
          dist=int((xchange**2+ychange**2)**.5)
          slope=[xchange/dist,ychange/dist]
          for x in range(1,dist):
            fout.write(str(spots[i-1][0]+slope[0]*x)+" "+str(spots[i-1][1]+slope[1]*x)+"\n")
        quit()
  screen.fill((0,0,0))
  screen.blit(image,(50,50))
  for item in spots:
    pg.draw.circle(screen,(255,0,0),item,5)
  pg.display.flip()
  clock.tick(60)
