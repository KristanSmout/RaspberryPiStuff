import time
import os
import subprocess
import platform
from cv2 import *
#import fswebcam

def Capture(ID):
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        namedWindow("cam-test")
        imshow("cam-test",img)
        waitKey(0)
        destroyWindow("cam-test")
        imwrite("Subject%s.jpg" %ID,img) #save image

#Program Header

print("------------------------")
print("Kristan's Webcam Capture")
print("------------------------")

#Init Testing

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

#Get Varibales

Name = input("Please enter subject's name: ")
PhotoMax = int(input("How Many Photo's Would you like to take? \n"))
PhotoFreq = int(input("How long do you want photo preperation time to be?      (Seconds) \n"))

savepath = (dir_path + "/" + Name)
#print(savepath)

try:  
    os.mkdir(savepath)
except OSError:  
    print ("Creation of the directory %s failed" % savepath)
    os.chdir(savepath)
   # print(os.getcwd())
else:  
    print ("Successfully created the directory %s " % savepath)
    os.chdir(savepath)
   # print(os.getcwd())


print("Starting Process")

print("Starting Process in 3 Seconds Please Prepare")
time.sleep(1)
print("Starting Process in 2 Seconds Please Prepare")
time.sleep(1)
print("Starting Process in 1 Seconds Please Prepare")
time.sleep(1)

print("Please Press Space To Continue To Next Image")


count = 0
while (count < PhotoMax):
 # os("fswebcam -r 1280x720 --no-banner Right1.jpg")
 print(count + 1)
 Capture(count + 1)
 time.sleep(PhotoFreq)
 count = count + 1
 #print(count + 1)
print ("Good bye!")
