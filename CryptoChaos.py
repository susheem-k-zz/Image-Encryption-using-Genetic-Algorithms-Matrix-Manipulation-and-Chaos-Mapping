import cv2
from math import sin,pi,floor
import numpy as np
from time import time
def chirikov(x):
    height,width=len(x),len(x[0])
    n=height
    K=10000000 #this parameter acts as the key.It decides the degree of deviation in the image
    newarray=np.zeros((height,width))
    newarray[0][0]=x[0][0]
    for i in range(height):
        for j in range(width):
            if (i+j)!=0:
                xnew=(i-1+j-1)%n
                ynew=(floor(j-1+K*sin(2*pi*xnew/n)))%n
                newarray[xnew][ynew]=x[i][j]
    for i in range(height):
        for j in range(width):
            x[i][j]=newarray[i][j]
    return x

def chirikovdec(x): #the decryption function
    height,width=len(x),len(x[0])
    n=height
    K=10000000#this parameter has to be equal to its counterpart in the encrypt function.
    newarray=np.zeros((height,width))
    newarray[0][0]=x[0][0]
    for i in range(height):
        for j in range(width):
            if (i+j)!=0:
                xnew=(floor(i-j+K*sin(2*pi*(i)/n)))%n
                ynew=(floor(j-K*sin(2*pi*(i)/n)))%n
                newarray[xnew][ynew]=x[i][j]
    for i in range(height):
        for j in range(width):
            x[i][j]=newarray[i][j]
    return x

if __name__=="__main__":
    x=cv2.imread("test.jpg",0)
    t1=time()
    x=chirikov(x)
    t2=time()
    #x=chirikovdec(x)
    t3=time()
    print(t2-t1,t3-t2)
    cv2.imwrite("output_Chaos.jpg",x)
    #cv2.imwrite("output_Chaos_decrypted.jpg",x)
    #cv2.imwrite("Output",x)

