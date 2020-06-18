# -*- coding: utf-8 -*-
"""
Created on 2020/6/28 14:23:32
@author: Later
内容：
1.选择图片
2.提取轮廓
3.填充字符
4.尺寸修改
"""
import cv2
import numpy as np
import copy

# 读取图片
img = cv2.imread('wx.png', cv2.IMREAD_GRAYSCALE)
# 显示图像尺寸信息
sp = img.shape
print(sp)
height = sp[0]
width = sp[1]
print(' width: %d \n height: %d \n' % (width, height))
# Candy算子做边缘检测
"""
cv2.Canny(image,            # 输入原图（必须为单通道图）
          threshold1, 
          threshold2,       # 较大的阈值2用于检测图像中明显的边缘
          )
"""
# todo:边缘检测时后续操作的关键,可继续优化
canny = cv2.Canny(img, 50, 100)  # 已经是二值图像了,但是此处是0和255
# 空模板
img_out = np.zeros(img.shape, np.uint8)
# 提取最外侧轮廓线(0=黑色,255=白色)
# 四次提取四个方向-叠加
for i in range(height):  # 左侧
    for j in range(width):
        if canny[i, j] == 255:
            img_out[i, j] = 255
            break  # 跳出内层循环
cv2.imshow('img_out', img_out)
for i in range(width):  # 上侧
    for j in range(height):
        if canny[j, i] == 255:
            img_out[j, i] = 255
            break  # 跳出内层循环
cv2.imshow('img_out', img_out)
for i in range(height):  # 右侧
    for j in range(width):
        if canny[i, width-j-1] == 255:
            img_out[i, width-j-1] = 255
            break  # 跳出内层循环
cv2.imshow('img_out', img_out)
for i in range(width):  # 下侧
    for j in range(height):
        if canny[height-1-j, i] == 255:
            img_out[height-1-j, i] = 255
            break  # 跳出内层循环
cv2.imshow('img_out', img_out)

# 绘图操作
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

# 判定是否为可填充方格
'''
左下角为需要的左边起点
hangID = height // 5
lieID = wight // 5
( hangID * 5 - 1 , lieID * 5 - 1 )
'''


#  添加文字: https://blog.csdn.net/sinat_29957455/article/details/88071078
#  cv2.putText(图像,需要添加字符串,需要绘制的坐标,字体类型,字号,字体颜色,字体粗细)
cv2.putText(canny, "WMNHQ Hello World", (0, 44), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 0, cv2.LINE_AA)
# todo: 对应字号和像素之间的关系,或者简化成三组对应供选择
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

