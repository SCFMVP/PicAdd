# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:23:32 2018
@author: Leon
内容：
对图片进行边缘检测；
添加滑动条，可自由调整阈值上下限。
@from: https://www.jb51.net/article/160479.htm
"""

import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow('Canny', 0)
# 创建滑动条
cv2.createTrackbar('minVal', 'Canny', 0, 255, nothing)
cv2.createTrackbar('maxVal', 'Canny', 0, 255, nothing)

# tip: some path questions
img = cv2.imread('qq.png', 0)

# 高斯滤波去噪
img = cv2.GaussianBlur(img, (3, 3), 0)
edges = img

k = 0
while 1:

    key = cv2.waitKey(50) & 0xFF
    if key == ord('q'):
        break
    # 读取滑动条数值
    minVal = cv2.getTrackbarPos('minVal', 'Canny')
    maxVal = cv2.getTrackbarPos('maxVal', 'Canny')
    edges = cv2.Canny(img, minVal, maxVal)

    # 拼接原图与边缘监测结果图
    img_2 = np.hstack((img, edges))
    cv2.imshow('Canny', img_2)

cv2.destroyAllWindows()