# -*- coding: utf-8 -*-
"""
@author: Mustafa Ünlü
@instagram: mmustafaunlu
@youtube: Kendi Çapında Mühendis
"""

import cv2
from matplotlib import pyplot as plt



resim = cv2.imread("kizkulesi.jpg",0)

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)

cv2.imshow("resim",resim)

cv2.imshow("resim penceresi",resim)


plt.imshow(resim,cmap="gray")
plt.show()


k = cv2.waitKey(0)


if k == 27:
    print("ESC tuşuna basıldı")
    
elif k == ord("q"):
    print("q tuşuna basıldı, resim kayıt edildi.")
    cv2.imwrite("kizkulesigri.jpg",resim)


# cv2.destroyWindow("resim penceresi")
cv2.destroyAllWindows()
