import cv2
import imutils
import numpy as np

rgb_img = cv2.imread('C:/1.jpg')
gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('origin image', imutils.resize(rgb_img, 800))
cv2.imshow('gray image', imutils.resize(gray_img, 800))
cv2.imwrite('rgb_img.jpg', rgb_img)
cv2.imwrite('gray_img.png', gray_img)

#等待一定时间自动销毁图像窗口
#if cv2.waitKey(10000):
#    cv2.destroyAllWindows()
#if cv2.waitKey(10000):
#    cv2.destroyWindow('origin image')

#接收特定键盘销毁图像窗口
#if cv2.waitKey(-1) == ord('A'):
#    cv2.destroyWindow('origin image')
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()