#python rotation creates a bigger box image and warps it, so it is very incorrect
#This monstrosity corrects it
import math
def rRotate(x,y,width,height,angle,axis): 
  offy=(width*abs(math.sin(angle*math.pi/180)))/2
  offx=(width*abs(math.cos(angle*math.pi/180)))/2
  a=[offy,offy+height*abs(math.cos(angle*math.pi/180)),offy+height*abs(math.cos(angle*math.pi/180)),offy][(int(angle//90+axis))%4]
  b=[offx,offx,offx+height*abs(math.sin(angle*math.pi/180)),offx+height*abs(math.sin(angle*math.pi/180))][(int(angle//90+axis))%4]
  return (x-b,y-a)
