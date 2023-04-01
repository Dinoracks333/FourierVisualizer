#draws the outline created by drawAccessory.py just for test purposes

import pygame as pg
pg.init()
fin=open("alexpic.out","r")
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
running=True
spots=[]
x=fin.readline()
while(x):
  spots.append([int(float(x)) for x in x.split()])
  x=fin.readline()
while(running):
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      pg.quit()
      quit()
  screen.fill((0,0,0))
  for item in spots:
    pg.draw.circle(screen,(255,0,0),item,2)
  pg.display.flip()
  clock.tick(60)