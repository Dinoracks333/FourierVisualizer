import math
def aTrig(c):
  length=(c.imag**2+c.real**2)**.5
  if(c.real>=0):
    if(c.imag>=0):
      q=0
    else:
      q=3
  else:
    if(c.imag>=0):
      q=1
    else:
      q=2
  xori,yori=math.acos(c.real/length),math.asin(c.imag/length) #just gets the angles in radians rn
  if(q>1):
    xori+=2*(math.pi-xori)
  if(q==3):
    yori+=2*math.pi
  if(q==1 or q==2):
    yori+=math.pi-yori*2
  return xori