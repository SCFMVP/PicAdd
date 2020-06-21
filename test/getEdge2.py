# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:23:32 2018
@author: Later
内容：
边缘检测(绘制效果好)
@from: https://www.cnblogs.com/denny402/p/5160955.html
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, draw

# # 生成二值测试图像
# img = np.zeros([100, 100])
# img[20:40, 60:80] = 1  # 矩形
# rr, cc = draw.circle(60, 60, 10)  # 小圆
# rr1, cc1 = draw.circle(20, 30, 15)  # 大圆
# img[rr, cc] = 1
# img[rr1, cc1] = 1

img = cv2.imread('qq.png', 0)
''''''
img2 = cv2.imread('E:\PycharmProjects\PicAdd\\assets\yellow\haitunyybailvyou.png')
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img2, contours, -1, (255, 0, 255), 3)
cv2.imshow("img", img2)


# 检测所有图形的轮廓
contours = measure.find_contours(img, 250)

# 绘制轮廓
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 8))
ax0.imshow(img, plt.cm.gray)
ax1.imshow(img, plt.cm.gray)
for n, contour in enumerate(contours):
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax1.axis('image')
ax1.set_xticks([])
ax1.set_yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

