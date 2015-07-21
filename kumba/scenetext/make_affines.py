import numpy as np
import cv2
import os
import matplotlib as plt
import re


def make_affines(image):
    img_name = image.split('.')[0]
    img_ext = image.split('.')[1]
    img=cv2.imread(image)
    cv2.imwrite(image, img)
    if img!=None:
        height, width = img.shape[:2]
        rows,cols,ch = img.shape

        pts1 = np.float32([[1444,652],[1594,2002],[2440,1930],[2326,586]])
            
        pts2 = np.float32([[1540,808],[1798,2122],[2350,1888],[2170,682]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=img_name+r'_0.'+img_ext #l
        cv2.imwrite(oname,dst)
            
        pts2 = np.float32([[1456,1486],[1642,2434],[2068,2092],[1972,1180]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=img_name+r'_1.'+img_ext #tl
        cv2.imwrite(oname,dst)
            
        pts2 = np.float32([[1174,1036],[1222,2152],[1966,2104],[2032,982]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=img_name+r'_2.'+img_ext #t
        cv2.imwrite(oname,dst)
            
        pts2 = np.float32([[1174,736],[1090,1786],[1690,2080],[1864,1054]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=img_name+r'_3.'+img_ext #tr
        cv2.imwrite(oname,dst)

            
        pts2 = np.float32([[1036,874],[1132,2116],[1786,2152],[1732,784]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=img_name+r'_4.'+img_ext #r
        cv2.imwrite(oname,dst)

            
        pts2 = np.float32([[1480,1156],[1396,1966],[1870,1948],[1942,1096]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[0][0],M[1][1] = 2*M[0][0],2*M[1][1]
        M[2][2]=1
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=img_name+r'_5.'+img_ext #br
        cv2.imwrite(oname,dst)

            
        pts2 = np.float32([[1408,892],[1450,1678],[2008,1612],[1948,814]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[0][0],M[1][1] = 2*M[0][0],2*M[1][1]
        M[2][2]=1
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=img_name+r'_6.'+img_ext #b
        cv2.imwrite(oname,dst)

            
        pts2 = np.float32([[1684,1258],[1786,1984],[2236,1978],[2152,1282]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=img_name+r'_7.'+img_ext #bl
        cv2.imwrite(oname,dst)
