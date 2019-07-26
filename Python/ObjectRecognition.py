# This code was implimented using the OpenCV tutorials by PythonProgramming.net
# A lot of it is not my own code. 
# The "Face and upper body recognition" section has a lot more of my own implimentation


import cv2
import numpy as np
import matplotlib.pyplot as plt

## FACE AND UPPER BODY RECOGNITION ########################

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
upper_body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
gest_cascade = cv2.CascadeClassifier('aGest.xml')

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

frames = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

        cv2.putText(img, "Face" , (x,y), font, 1, (255,0,0), 1, cv2.LINE_AA)

        # roi_gray = gray[y:y+h, x:x+w]
        # roi_color = img[y:y+h, x:x+w]

    upper_body = upper_body_cascade.detectMultiScale(gray)
    for (bx,by,bw,bh) in upper_body:
        cv2.rectangle(img, (bx,by), (bx+bw, by+bh), (0,0,255), 2)
        cv2.putText(img, "Upper Body" , (bx,by), font, 1, (0,0,255), 1, cv2.LINE_AA)

    gest = gest_cascade.detectMultiScale(gray)
    for (gx,gy,gw,gh) in gest:
        cv2.rectangle(img, (gx,gy), (gx+gw, gy+gh), (0,0,255), 2)
        cv2.putText(img, "Gest" , (gx,gy), font, 1, (0,0,255), 1, cv2.LINE_AA)

    frames += 1
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    #escape key
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

####################################################

# ## FACE AND EYE RECOGNITION ########################

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# upper_body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

# cap = cv2.VideoCapture(0)
# font = cv2.FONT_HERSHEY_SIMPLEX

# frames = 0
# while True:
#     ret, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

#         cv2.putText(img, "Face" , (x,y), font, 1, (255,0,0), 1, cv2.LINE_AA)

#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray)
#         eye_count = 1
#         first_eye = (None,None)
#         for (ex,ey,ew,eh) in eyes:
#             if eye_count > 2:
#                 break
#             #centre of the first eye does not line up
#             if eye_count == 2:    
#                 print(abs(first_eye[1]-eh))
#                 if (first_eye[0] > (ey+eh+ey)/2 > first_eye[0]+first_eye[1]):# or abs(first_eye[1]/eh) < 0.6:
#                     continue
#             cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
#             cv2.putText(roi_color, "Eye" , (ex,ey), font, 1, (0,255,0), 1, cv2.LINE_AA)
#             eye_count += 1
#             first_eye = (ey,eh)
#     #cv2.putText(img, str(frame)+str(abs(first_eye[1]-eh)), (100,100), font, 1, (0,255,0), 1, cv2.LINE_AA)
#     frames += 1
    
#     cv2.imshow('img',img)
#     k = cv2.waitKey(30) & 0xff
#     #escape key
#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

# ####################################################

### IMAGE ARITHMATIC AND THRESHOLDING###############

# #identical size images
# img1 = cv2.imread('3D-Matplotlib.png')
# #img2 = cv2.imread('mainsvmimage.png')
# img2 = cv2.imread('mainlogo.png')

# ##adding images
# #add = img1 + img2
# #looks fine
# #add = cv2.add(img1,img2)
# #adds individual pixel values, >255 == 255

# #how much each image contributes to the image,  last term is gammma
# #weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

# #1 threshold
# rows,cols,channels = img2.shape
# roi = img1[0:rows,0:cols]
# #2 create a mask of the logo
# img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# #bianary threshold, a 0 or 1, if pixel is >220, convert to 255
# #<220 turn to black, all inversed
# ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
# #created a black and white image
# #the black are of the mask
# #bitwise is a low level logic system
# mask_inv = cv2.bitwise_not(mask)
# img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# dst = cv2.add(img1_bg, img2_fg)
# img1[0:rows,0:cols] = dst

# cv2.imshow('res', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#####################################################


### Region of Image and changing the pixels ########

# img = cv2.imread('watchsml.jpg', cv2.IMREAD_COLOR)

# img[55,55] = [255,255,255]
# px = img[55,55]

# #Region of Image (roi)- subimage of an image
# img[100:150, 100:150] = [255,255,255]

# watch_face = img[200:375, 180:320]
# #difference 175, 140
# img[0:175, 0:140] = watch_face


# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

####################################################

###DRAWING ON AN IMAGE##############################

# img = cv2.imread ('watch.jpg', cv2.IMREAD_COLOR)

# #uses BGR not RGB
# cv2.line (img, (0,0), (500,500), (0,255,0), 15)
# cv2.rectangle(img, (150,250), (2000,1500), (0,255,0), 5)
# cv2.circle(img, (100, 63), 100, (255,0,0), -1)

# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# #pts. pts.reshape((-1,1,2))
# cv2.polylines(img, [pts], True, (255,255,0))

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, "YEET" , (200,300), font, 1, (200,255,255), 2, cv2.LINE_AA)

# cv2.imshow('image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


####################################################

###READ VIDEO#######################################

# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

# while True:
#     #return is 0 or 1, and the frame
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     out.write(frame)
#     cv2.imshow("frame", frame)
#     cv2.imshow("gray", gray)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()

##################################################
###READ IMAGE#####################################

#instead of RGB+alpha, we just use greyscale (0)
#img = cv2.imread("watch.jpg", cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50,100],[80,100], 'c', linewidth=5)
# plt.show()

##############################################