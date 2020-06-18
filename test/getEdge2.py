# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:23:32 2018
@author: Later
内容：
边缘检测
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

img = cv2.imread('key.jpg', 0)
# 检测所有图形的轮廓
contours = measure.find_contours(img, 0.5)

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

