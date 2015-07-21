import numpy as np
import cv2
import os
import matplotlib as plt
import re
orb = cv2.ORB()

imagesFolder=r"./NEC-cropped/train"
os.chdir(imagesFolder)
images=os.listdir(".")
for i in images:
    imgn = i
    imgn = re.sub(r".jpg",'',imgn)
    img=cv2.imread(i)
    if img!=None:
        height, width = img.shape[:2]
##        while (height>1000 and width>1000):
##            img = cv2.resize(img,(width/2, height/2), interpolation = cv2.INTER_AREA)
##            height, width = img.shape[:2]
        rows,cols,ch = img.shape
        pts1 = np.float32([[1444,652],[1594,2002],[2440,1930],[2326,586]])
        
        pts2 = np.float32([[1540,808],[1798,2122],[2350,1888],[2170,682]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        print M
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=imgn+r'_0'+'.jpg' #l
        cv2.imwrite(oname,dst)
        
        pts2 = np.float32([[1456,1486],[1642,2434],[2068,2092],[1972,1180]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        print M
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=imgn+r'_1'+'.jpg' #tl
        cv2.imwrite(oname,dst)
        
        pts2 = np.float32([[1174,1036],[1222,2152],[1966,2104],[2032,982]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        print M
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=imgn+r'_2'+'.jpg' #t
        cv2.imwrite(oname,dst)
        
        pts2 = np.float32([[1174,736],[1090,1786],[1690,2080],[1864,1054]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        print M
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=imgn+r'_3'+'.jpg' #tr
        cv2.imwrite(oname,dst)

        
        pts2 = np.float32([[1036,874],[1132,2116],[1786,2152],[1732,784]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        print M
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=imgn+r'_4'+'.jpg' #r
        cv2.imwrite(oname,dst)

        
        pts2 = np.float32([[1480,1156],[1396,1966],[1870,1948],[1942,1096]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[0][0],M[1][1] = 2*M[0][0],2*M[1][1]
        M[2][2]=1
        print M
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=imgn+r'_5'+'.jpg' #br
        cv2.imwrite(oname,dst)

        
        pts2 = np.float32([[1408,892],[1450,1678],[2008,1612],[1948,814]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[0][0],M[1][1] = 2*M[0][0],2*M[1][1]
        M[2][2]=1
        print M
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=imgn+r'_6'+'.jpg' #b
        cv2.imwrite(oname,dst)

        
        pts2 = np.float32([[1684,1258],[1786,1984],[2236,1978],[2152,1282]]) #lt,lb,rb,rt
        M = cv2.getPerspectiveTransform(pts1,pts2)
        M[0][2],M[1][2] = 0,0
        M[2][0],M[2][1] = 0,0
        M[2][2]=1
        print M
        dst = cv2.warpPerspective(img,M,(cols,rows))
        oname=imgn+r'_7'+'.jpg' #bl
        cv2.imwrite(oname,dst)
