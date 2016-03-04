import sys
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average
import cv2
from matplotlib import pyplot as plt

def main():
    path = "C:\Users\Ivan\Desktop\Imagenes"  

    path1='C:\Users\Ivan\Desktop\Imagenes\Aaron_Peirsol_0001.jpg'
    path2='C:\Users\Ivan\Desktop\Imagenes\Aaron_Peirsol_0004.jpg'
    img = to_grayscale(cv2.imread(path1,0))
    imge = to_grayscale(cv2.imread(path2,0))
    img1 = to_grayscale(imread(path1,0))
    img2 = to_grayscale(imread(path2,0))

    # global thresholding
    ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret11,th11 = cv2.threshold(imge,127,255,cv2.THRESH_BINARY)
# Otsu's thresholding
    ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret22,th22 = cv2.threshold(imge,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(img,(5,5),0)
    blur1 = cv2.GaussianBlur(imge,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret33,th33 = cv2.threshold(blur1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
    images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3,
          imge, 0, th11,
          imge, 0, th22,
          blur1, 0, th33]
    
    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

    for i in xrange(1):
       
            plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
            #plt.subplot(3,3,j*3+1),plt.imshow(images[j*3],'gray')
            #plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
            plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
            #plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
            plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
            #plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    
    plt.show()

    #imge = cv2.imread('C:\Users\Ivan\Desktop\Imagenes\Aaron_Peirsol_0002.jpg',0)


    # global thresholding
    ret11,th11 = cv2.threshold(imge,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
    ret22,th22 = cv2.threshold(imge,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
    blur1 = cv2.GaussianBlur(imge,(5,5),0)
    ret33,th33 = cv2.threshold(blur1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
    images = [imge, 0, th11,
          imge, 0, th22,
          blur1, 0, th33]
    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

    for i in xrange(1):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    #plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    #plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    #plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    
    plt.show()
    
    
    # compare
    im1, im2 = compare_images(img1, img2)
    t1 = im1/img1.size
    t2 = (im2*1.00/img2.size)*100
    if t1 != 0:
        if t2 != 0:
            print "Foto 1:", im1, "/ Tot. pixel:", t1
            print "Foto 2:", im2, "/ Tot. pixel:", t2
    porcent=t1-t2
    norm=im1-im2
    if porcent == 0:
        porcent=100
        print "Similitud Encontrada %",porcent
    else:
        print "Similitud Encontrada %",((1-(porcent/100))*100)   
def compare_images(img1, img2):
    # normalize to compensate for exposure difference
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # element wise for scipy arrays
    m_norm = sum(abs(diff))  #  norm
    z_norm = norm(diff.ravel())  # Zero norm
    res=m_norm-z_norm
    return (m_norm, z_norm)

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

if __name__ == "__main__":
    main()
