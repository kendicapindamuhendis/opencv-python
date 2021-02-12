# -*- coding: utf-8 -*-
"""
@author: Mustafa Ünlü
@instagram: mmustafaunluu
@youtube: Kendi Çapında Mühendis
"""

import cv2
import numpy as np


img = cv2.imread("image_2.jpg")


print(img.shape)

rows,cols = img.shape[:2]

click_count = 0
a = []

dst_points = np.float32([
    [0,0],
    [cols-1,0],
    [0,rows-1],
    [cols-1,rows-1]])

cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.namedWindow("output",cv2.WINDOW_NORMAL)

def draw(event,x,y,flags,param):
    global click_count,a
    
    if click_count < 4:
        
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print(click_count)
            print(x,y)
            click_count += 1
            a.append((x,y))
    else:
        
        src = np.float32([
            [a[0][0],a[0][1]],
            [a[1][0],a[1][1]],
            [a[2][0],a[2][1]],
            [a[3][0],a[3][1]]])
        
        click_count = 0
        a = []
        
        M = cv2.getPerspectiveTransform(src,dst_points)
        img_output = cv2.warpPerspective(img, M, (cols,rows))
        
        img_output = cv2.cvtColor(img_output,cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(img_output,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY,11,1)
        cv2.imshow("output",thresh)

    pass


cv2.setMouseCallback("img",draw)


while(1):
    cv2.imshow("img",img)
    # cv2.imshow("img_output",img_output)    
    if cv2.waitKey(1) == ord("q"):
        break
    
    
cv2.destroyAllWindows()
