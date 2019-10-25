import numpy as np
import cv2
from time import time
def encrypt(A): #A is the image matrix
  n = len(A)
  M = A
  i = 0
  swap=[] #stores the swapping information
  modify=[] #stores the modification/subtraction data
  for k in range(n-1):
   modify.append([])
   swap.append([])
   for i in range(k,n):
     if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i],M[k]
        swap[k].append((k,i))
     else:
        pass
   for j in range(k+1,n):
       q = float(M[j][k]) / M[k][k]
       modify[k].append(q)
       for m in range(k, n):
           M[j][m] = M[j][m] -  q * M[k][m]
  
  return [M,swap,modify]

def decrypt(M,swap,modify):
    n=len(M)
    swap.reverse() #Apply the same operations in reverse
    modify.reverse()
    for k in range(n-2,-1,-1):
        index=0
        for dummy in range(k+1,n):
            for j in range(0,n):
                M[dummy][j]+=modify[n-2-k][index]*M[k][j]
            index+=1
        for (i,j) in list(reversed(swap[n-2-k])):
            M[i],M[j]=M[j],M[i]
    return M          

if __name__=="__main__":
    mtx = cv2.imread(r"test.jpg",0)
    mtx=mtx.tolist()
    t1=time()
    mtx,swap,modify=encrypt(mtx)
    t2=time()
    #mtx=decrypt(mtx,swap,modify)
    t3=time()
    mtx=np.array(mtx)
    print(t2-t1,"  ",t3-t2)
    #cv2.imwrite(r'output_PartialPivot_decrypted.jpg',mtx)
    cv2.imwrite(r'output_PartialPivot.jpg',mtx)

