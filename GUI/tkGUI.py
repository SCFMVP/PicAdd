# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import filedialog, CENTER, W, END

import cv2
import numpy as np
from PIL import Image, ImageTk
"""
Tip: 
1. 路径不可以有中文
2. 只针对单体轮廓
3. 黑色轮廓无效
ps: 从MATLAB到Python不太习惯,感觉MATLAB更方便
"""

'''实例化root窗体'''
window = tk.Tk()
window.title('图形识别填充 V1.0')
window.geometry('550x800')  # 这里的乘是小x   wigth * height
window.configure(bg='#696969')

'''定义全局变量'''
picPath = 'qq.png'
img_original = ''
img_edge = ''
img_result = ''
cv_img = ''
canny = ''
img_out = ''
img_color = ''
'''回调函数'''
def get_edge():
    global img_edge, canny, img_result, cv_img, img_color, img_out
    canny = cv2.Canny(cv_img, 50, 100)  # 已经是二值图像了,但是此处是0和255
    '''填充白色'''
    img_out = np.zeros(canny.shape, np.uint8)  # 二值图像
    img_color = np.zeros(cv_img.shape, np.uint8)  # 彩色图像
    sp = canny.shape
    height = sp[0]
    width = sp[1]
    # 白底图片
    for i in range(height):  # 左侧
        for j in range(width):
            img_color[i, j] = (255, 255, 255)
    '''# 提取最外侧轮廓线(0=黑色,255=白色)'''
    # 四次提取四个方向-叠加
    # todo: 判断单方向连续(这是需要保留的), 算法有缺陷
    for i in range(height):  # 左侧
        for j in range(width):
            if canny[i, j] == 255:
                img_out[i, j] = 255
                # img_color[i, j] = (255, 0, 0)
                # 这里坐标与上面的不一致的
                cv2.putText(img_color, '*', (j, i), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 0, 5)
                print(i)
                break
                # if canny[i, j+1] != 255:
                #     break  # 跳出内层循环
            else:
                img_out[i, j] = 255
    # cv2.imshow('left', img_out)
    for i in range(width):  # 上侧
        for j in range(height):
            if canny[j, i] == 255:
                img_out[j, i] = 255
                # img_color[j, i] = (255, 0, 0)
                cv2.putText(img_color, '*', (i, j), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 0, 5)
                break  # 跳出内层循环
            else:
                img_out[j, i] = 255
    # cv2.imshow('up', img_out)
    for i in range(height):  # 右侧
        for j in range(width):
            if canny[i, width - j - 1] == 255:
                img_out[i, width - j - 1] = 255
                # img_color[i, width - j - 1] = (255, 0, 0)
                cv2.putText(img_color, '*', (height - 1 - j, i), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 0, 5)
                break  # 跳出内层循环
            else:
                img_out[i, width - j - 1] = 255
    # cv2.imshow('right', img_out)
    for i in range(width):  # 下侧
        for j in range(height):
            if canny[height - 1 - j, i] == 255:
                img_out[height - 1 - j, i] = 255
                # img_color[height - 1 - j, i] = (255, 0, 0)
                cv2.putText(img_color, '*', (i, width - j - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 0, 5)
                break  # 跳出内层循环
            else:
                img_out[height - 1 - j, i] = 255
    cv2.imshow('right', img_out)
    # cv2.imshow('right', img_color)
    # 显示边缘轮廓
    image = Image.fromarray(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
    # todo: 做个更好的resize
    image = image.resize((200, 200), Image.ANTIALIAS)
    img_edge = ImageTk.PhotoImage(image)  # img_new必须使用全局变量, 否则会显示为背景色
    label_img2.configure(image=img_edge)



def get_result():
    global canny, img_result, cv_img, img_out, img_color
    sp = canny.shape
    height = sp[0]
    width = sp[1]
    # 绘图操作
    point_color = (66, 66, 66)  # BGR
    thickness = 1
    lineType = 4
    strSize = 8  # 字符size: strSize*strSie
    '''判断可用方格'''
    # 二值图像 (0=黑色,255=白色)
    isWhite = 0
    hangID = []
    lieID = []
    p = 0
    for i in range(height // strSize):
        for j in range(width // strSize):  # 遍历 i * j 个小格
            isWhite = 0
            for m in range(strSize):
                for n in range(strSize):  # 遍历小格内 m * n 个像素
                    if img_out[m + i * strSize, n + strSize * j] == 255:  # 检测到白色像素则标记为无线方格并跳出循环
                        isWhite = 1
                        break
                    if isWhite != 1 and m == strSize - 1 and n == strSize - 1:
                        hangID.append(m + i * strSize)  # 此处为方格左下角坐标, 只能使用append!
                        lieID.append(strSize * j)
                        # todo: 可以直接在此处进行填充, 还要考虑大小问题
                        # cv2.putText(img_out, "W", (strSize * j, m + i * strSize), cv2.FONT_HERSHEY_SIMPLEX, 0.25,
                        #             (66, 66, 66), 0,
                        #             cv2.LINE_AA)
                if isWhite == 1:
                    break
    print('hangID:', hangID)
    print('lieID:', lieID)
    print('可用方格数: ' + str(len(hangID)))
    '''填充文字'''
    strData = eStr.get('1.0', END)
    # print('strData:', strData)
    print('可用字符数:', len(strData))
    for i in range(len(hangID)):
        if i >= len(strData):
            cv2.putText(img_out, ' ', (lieID[i], hangID[i]), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (66, 66, 66), 0, cv2.LINE_AA)
        else:
            data = str(strData).replace('\n', ' ')  # 去换行符
            cv2.putText(img_out, data[i], (lieID[i], hangID[i]), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (66, 66, 66), 0, cv2.LINE_AA)
    # cv2.imshow('str', img_out)
    # cv2.imshow('str', img_color)
    # 以下用于显示
    image = Image.fromarray(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
    # todo: 做个更好的resize
    image = image.resize((200, 200), Image.ANTIALIAS)
    img_result = ImageTk.PhotoImage(image)  # img_new必须使用全局变量, 否则会显示为背景色
    # todo: 越描越黑问题
    label_img3.configure(image=img_result)
    cv2.imwrite('1.png', img_color)


def get_picPath(event):
    global picPath, img_original, cv_img
    picPath = filedialog.askopenfilename()  # 获得选择好的文件
    print('Filepath:', picPath)
    cv_img = cv2.imread(picPath)
    cv2.imshow('1 canny', cv_img)
    sp = cv_img.shape
    print('imgInfo:', sp)
    height = sp[0]
    width = sp[1]
    # 更新像素值显示
    lb5.configure(text='Width ： '+str(width)+' pt    Height ： '+str(height)+' pt')
    # 更新图片
    '''二者都可以
    real: E:\PycharmProjects\PicAdd\GUI\wx.png
    this: E:/PycharmProjects/PicAdd/GUI/wx.png
    '''
    image = Image.open(picPath)
    # todo: 做个更好的resize
    image = image.resize((200, 200), Image.ANTIALIAS)
    img_original = ImageTk.PhotoImage(image)  # img_new必须使用全局变量, 否则会显示为背景色
    # img_new = img_new.zoom(2, 1)  # 放大-只支持整数倍
    # img_new = img_new.subsample(9, 9)  # 缩小
    label_img1.configure(image=img_original)


'''
绘制控件布局
'''
# ==================选择图片=================
# 提示标签
lb1 = tk.Label(window,  text='选择图片:', bg='#696969', fg='white', font=('Arial', 10), width=30, height=2)
# # 选择图片画布
cv_img = cv2.imread('qq.png')
img1 = Image.open('qq.png')
img1 = img1.resize((200, 200), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)  # img_new必须使用全局变量, 否则会显示为背景色
label_img1 = tk.Label(window, image=img1,  bg='#888888', justify='center', anchor='n')
label_img1.bind("<Button-1>", get_picPath)  # 绑定鼠标左击事件
lb1.grid(row=0, column=0)
label_img1.grid(row=1, column=0)
# ==================输入字符=================
# 提示标签
lb2 = tk.Label(window, text='填充内容:', bg='#696969',  fg='white', font=('Arial', 10))
# 字符输入框
eStr = tk.Text(window, show=None, bg='#696969', fg='white',  font=('Arial', 8), height=14, width=40)   # 显示成密文形式
lb2.grid(row=0, column=1)
eStr.grid(row=1, column=1)
# ==================确定轮廓=================
# 提示标签
lb3 = tk.Label(window, text='确定轮廓:', bg='#696969',  fg='white', font=('Arial', 10), width=30, height=2)
# 轮廓画布
img2 = Image.open('qq.png')
img2 = img2.resize((200, 200), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
label_img2 = tk.Label(window, image=img2,  bg='#888888', justify='center', anchor='n')
lb3.grid(row=2, column=0)
label_img2.grid(row=3, column=0)
# ==================设置像素=================
lb4 = tk.Label(window, text='像素值:', bg='#696969',  fg='white', font=('Arial', 10), width=30, height=2)
lb4.grid(row=2, column=1)
# ==================设置颜色=================
lb5 = tk.Label(window, text='Width： 200 pt  Height： 200 pt', bg='#696969',  fg='white', font=('Arial', 12), width=30, height=2)
lb5.grid(row=3, column=1)
# ==================填充字符=================
# 提示文字
lb6 = tk.Label(window, text='生成结果:', bg='#696969',  fg='white', font=('Arial', 10), width=30, height=2)
# lb6.pack()
# 按钮
btn1 = tk.Button(window, text='生成轮廓', font=('Arial', 12), width=10, height=1, command=get_edge)
btn2 = tk.Button(window, text='生成结果', font=('Arial', 12), width=10, height=1, command=get_result)
# 结果画布
img3 = Image.open('qq.png')
img3 = img3.resize((200, 200), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img3)
label_img3 = tk.Label(window, image=img3,  bg='#888888', justify='center', anchor='n')

lb6.grid(row=4, column=0)
btn1.grid(row=4, column=1)
btn2.grid(row=5, column=1)
label_img3.grid(row=5, column=0)

'''主窗口循环显示'''
window.mainloop()
