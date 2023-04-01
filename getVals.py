import math
from invTrig import aTrig
fin=open("dangVals.out","r")
out=open("dang.out","w")
num_arrs=500
fx=[]
x=fin.readline()
while(x):
  x=x.split()
  fx.append(complex(float(x[0]),-float(x[1])))
  x=fin.readline()
#note that im subtracting by the y vals bc
#y is flipped on a computer screen
def getVal(fx,c): #discrete fourier transform, essentially a numeric integral
  sSize=1/len(fx)
  tot=0
  for i in range(len(fx)):
    tot+=sSize*fx[i]*math.e**((-1)**.5*2*math.pi*-c*i/len(fx))
  return tot 
arrows=[getVal(fx,0)]
out.write(str(num_arrs)+"\n")
out.write(str((arrows[-1].imag**2+arrows[-1].real**2)**.5)+" "+str(aTrig(arrows[-1]))+"\n")
for i in range(2,num_arrs+2):
  arrows.append(getVal(fx,i//2*(i%2*2-1)))
  length=(arrows[-1].real**2+arrows[-1].imag**2)**.5
  out.write(str(length)+" "+str(aTrig(arrows[-1]))+"\n")
out.close()
