#from https://youtu.be/nnH55-zD38I?list=PL45ldJ70zlhchPnWsDn3dVXkOWUtG-TDX

#run and test tensorflow and cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print('Work directory is ', os.getcwd())
import tensorflow as tf
print('Tensorflow version is ', tf.__version__)
import cv2
print('OpenCV version is ', cv2.__version__)

#project modules
import numpy as np

#DATA_DIR = os.path.join(os.getcwd(), 'Data/Murtaza')
DATA_DIR = os.path.join('/Users/johnlennon/My Drive/Python/Pdf/data/Murtaza_img')

#download images
img1 = cv2.imread(f'{DATA_DIR}/Train/Phone.jpg')
img2 = cv2.imread(f'{DATA_DIR}/Test/CaptureImage.jpg')
#img2 = cv2.imread(f'{DATA_DIR}/202011.8.jpg')


#oriented brief -features detections
#descriptor is -500 features on deafault in 32 values
orb = cv2.ORB_create(nfeatures=1000)

#key points and descriptions
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
print('description1 dimention', des1.shape)
print('description1 dimention', des2.shape)
#compare des1 500features and des2 features with each other
#brootforce mather
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
print('len of matches', len(matches))
#k=2 two values compare

#look good distantion between two values

good = []
for m, n in matches:
    if m.distance < 0.9*n.distance:
        good.append([m])

#draw two pictures with matches
if good:
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
    cv2.imshow('Img1', img1)
    cv2.imshow('Img2', img2)
    cv2.imshow(str(len(good)), img3)
else:
    print('list is empty')

#show kp
# imgKp1 = cv2.drawKeypoints(img1, kp1, None)
# imgKp2 = cv2.drawKeypoints(img2, kp2, None)

# cv2.imshow('Kp1', imgKp1)
# cv2.imshow('Kp2', imgKp2)

#close windows
cv2.waitKey(0)
cv2.destroyAllWindows()

