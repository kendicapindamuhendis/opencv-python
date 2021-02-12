# -*- coding: utf-8 -*-
"""
@author: Mustafa Ünlü
@instagram: mmustafaunluu
@youtube: Kendi Çapında Mühendis
"""
import cv2

img1 = cv2.imread("cv2.png")
img2 = cv2.imread("r.jpg")

x,y,z = img1.shape
roi = img2[0:x,0:y]


img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1_gray,10,255,cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg = cv2.bitwise_and(img1,img1,mask=mask)

toplam = cv2.add(img1_bg,img2_fg)

img2[0:x,0:y] = toplam

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
cv2.imshow("resim",img2)
cv2.imshow("resim2",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()
