import cv2       #importing cv2
import cvzone    #This will import numpy and opencv
# We have also installed package MediaPipe

#Wrapper package to remove background
from cvzone.SelfiSegmentationModule import SelfiSegmentation

#Importing to get images
import os

#Creating object to get access to Webcamera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width(3)
cap.set(4, 480)  # Height(4)
cap.set(cv2.CAP_PROP_FPS, 60) #setting frame rate
#create selfie segmentation object
segmentor = SelfiSegmentation()  #0 for generalized 1 (default) for landscape
fpsReader = cvzone.FPS()  #Write FPS on image


#List down all images in Directory from Image folder
listImg = os.listdir("Images")
print(listImg)
imgList = []

for imgPath in listImg:
    img = cv2.imread(f'Images/{imgPath}')
    imgList.append(img)
print(len(imgList))


indexImg = 0


while True:
    #takes image from webcam
    success, img = cap.read()

    #Remove background and put background
    #if threshold = 1 , whole image will be background
    imgOut = segmentor.removeBG(img,imgList[indexImg],threshold=0.8)

    #Output Image stack
    imgStacked = cvzone.stackImages([img,imgOut],2,1)

    #to display FPS on stacked Image
    _, imgStacked = fpsReader.update(imgStacked,color=(0,0,255))

    #runs webcam output
    cv2.imshow("Image",imgStacked)
    # cv2.imshow("Image",img)
    # cv2.imshow("Image Out",imgOut)
    key = cv2.waitKey(1)

    #Giving Keyboard key 'a' to go prev background pic
    if key ==ord('a'):
        if indexImg > 0:
            indexImg -= 1
    #Giving Keyboard key 'd' to go next background pic
    elif key == ord('d'):
        if indexImg < len(imgList) -1 :
            indexImg += 1

    # Coming out of program
    elif key == ord('q'):
        break


