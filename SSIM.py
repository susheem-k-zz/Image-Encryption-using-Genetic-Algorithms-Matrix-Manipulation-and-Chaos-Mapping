from skimage.measure import compare_ssim as ssim
import cv2
x='PartialPivot' #select the algorithm being tested
im1=cv2.imread(r'..//Data//test.jpg',0)
im2=cv2.imread(r'..//Results//output_'+x+'_decrypted.jpg',0)
im3=cv2.imread(r'..//Results//output_'+x+'.jpg',0)
print(ssim(im1,im2))
print(ssim(im1,im3))