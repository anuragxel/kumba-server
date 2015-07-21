import numpy as np
import cv2, pickle
import os
from scenetext.models import *
from kumba.settings import BASE_DIR
from django.core.management import BaseCommand

class Command(BaseCommand):
        def handle(self, *args, **options):
                orb = cv2.ORB()
		frequency = {}

                fs = Image.objects.all().order_by('id')
                l = len(fs)
                filenames = []
                for i in range(l):
                        filenames.append((fs[i]).image.path)
			if fs[i].image_class not in frequency.keys():
				frequency[fs[i].image_class] = 1
			else:
			 	frequency[fs[i].image_class] = frequency[fs[i].image_class] + 1

                des=[]
                c1=0
                for image in filenames:
                        img = cv2.imread(image)
                        if img!=None:
                                kp1, des1 = orb.detectAndCompute(img,None)
                                des.append(des1)
                                c1=c1+1
                                print c1,"out of",len(filenames)

                with open('/home/cloudstrife/Documents/kumbathon/kumba/scenetext/orb.pickle', 'wb') as f:
                        pickle.dump([des, filenames, frequency], f, protocol=-1)
