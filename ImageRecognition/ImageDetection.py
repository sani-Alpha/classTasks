#importing cv2
import cv2

#enabling access to camera for capture
cap=cv2.VideoCapture(0)

#capturing images
tp1=cap.read()[1]
tp2=cap.read()[1]
tp3=cap.read()[1]

#finding difference between images
def image_diff(x,y,z):
    dif1=cv2.subtract(tp1,tp2)
    dif2=cv2.subtract(tp2,tp3)
    dif=cv2.subtract(dif1,dif2)
    return dif

#checing if the object is still or if thers a motion
img=image_diff(tp1,tp2,tp3)
b,g,r=cv2.split(img)
if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
    print("still object detected")
else:
    print("motion detected")

#displaying all the images
cv2.imshow('p1',tp1)
cv2.imshow('p2',tp2)
cv2.imshow('p3',tp3)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWidnows()
