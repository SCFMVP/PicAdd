# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:23:32 2018
@author: Later
内容：
填充字符串
@from:
"""
import cv2
from PIL import Image,ImageDraw

img = cv2.imread('qq.png', cv2.IMREAD_GRAYSCALE)
# 显示图像尺寸信息
sp = img.shape
print(sp)
height = sp[0]
width = sp[1]
print(' width: %d \n height: %d \n' % (width, height))

# Candy算子-----貌似效果最好
canny = cv2.Canny(img, 50, 100)

point_color = (66, 66, 66)  # BGR
thickness = 1
lineType = 4
strSize = 5  # 字符size: strSize*strSie
# 绘制网格
for i in range(height//strSize):
    lineId = i*strSize
    ptStart = (0, lineId)  # 画横线
    ptEnd = (width, lineId)
    cv2.line(canny, ptStart, ptEnd, point_color, thickness, lineType)
for i in range(width//strSize):
    lineId = i*strSize
    ptStart = (lineId, 0)  # 画竖线
    ptEnd = (lineId, height)
    cv2.line(canny, ptStart, ptEnd, point_color, thickness, lineType)

#  添加文字: https://blog.csdn.net/sinat_29957455/article/details/88071078
#  cv2.putText(图像,需要添加字符串,需要绘制的坐标,字体类型,字号,字体颜色,字体粗细)
cv2.putText(canny, "WMNHQ Hello World", (0, 44), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 0, cv2.LINE_AA)
# todo: 对应字号和像素之间的关系
"""
5*5像素划分的小格子
2个小格子对应一个0.5号字体
"""
# todo: 改为单字符填充,不要一起填充(肯造成坐标文字不对应)

# 显示图像
# todo:在原图上标注
cv2.namedWindow('canny', 0)
cv2.resizeWindow('canny', width, height)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

