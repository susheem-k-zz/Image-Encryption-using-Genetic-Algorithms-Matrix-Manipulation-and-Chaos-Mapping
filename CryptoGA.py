import cv2
import numpy as np
from time import time
def prg(seed,iters,l):
    op=seed
    while iters:
        op=(29*seed+13)%l
        seed=op
        iters-=1
    return op
        
        
def getrvals(x,l):
    r1=0
    r2=0
    width,height=len(x[0]),len(x)
    for i in range(0,height):
        for j in range(0,width):
            r1+=pow(-1,i+j)*x[i][j]
            r2+=pow(-1,i+j+1)*x[i][j]
    return abs(r1//(height*l)),abs(r2//(height*l))

def createvectors(x,l):
    frags_per_row=len(x[0])//l
    vecs=[]
    for dummyvecs in x:
        for i in range(0,frags_per_row):
            vecs.append(dummyvecs[i*l:(i+1)*l])
    return vecs       

def crossover(vector,x,y,l):
    if x<l and y<l:
        coi=x
    else:
        coi=0
    coiter=(3*x+5*y)%l
    for j in range(0,2*coiter,2):
        n1=prg(coi,j,l)
        n2=prg(coi,j+1,l)
        temp=vector[n1]
        vector[n1]=vector[n2]
        vector[n2]=temp
    return vector
def mutate(vector,x,y,l):
    if x<l and y<l:
        mui=y
    else:
        mui=0
    muiter=(5*x+73*y)%l
    for j in range(0,muiter):
        n1=prg(mui,j,l)
        vector[n1]=255-vector[n1]
    return vector
if __name__=="__main__":
    x=cv2.imread("..//Data//test.jpg",0)
    #x=cv2.imread("..//Results//output_GA.jpg",0)
    x=cv2.resize(x,(256,256))
    frags_per_row=1
    width,height=len(x[0]),len(x)
    l=width//frags_per_row
    r1,r2=20,30
    t1=time()
    vecs=createvectors(x,l)
    for i in range(0,len(vecs)):
        vecs[i]=crossover(vecs[i],r1,r2,l)
        vecs[i]=mutate(vecs[i],r1,r2,l)
        r1+=1
        r2+=1
    crypt=np.zeros((height,width))
    count=0
    for i in range(0,len(crypt)):
        dummy=np.append([],vecs[count*frags_per_row:(count+1)*frags_per_row])
        count+=1
        crypt[i]=dummy
    t2=time()
    print(t2-t1)
    cv2.imwrite("..//Results//output_GA.jpg",x)
    #cv2.imwrite("..//Results//output_GA_Decrypted.jpg",x)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
        
        
