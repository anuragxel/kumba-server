from django.shortcuts import render, render_to_response
import numpy as np
import cv2
import os, operator
import re
import json
import pickle
from django.http import HttpResponse
from django.template import RequestContext
from scenetext.forms import *
from scenetext.models import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from scenetext.models import *
from django.views.decorators.csrf import csrf_exempt
import goslate
from django.http import JsonResponse

#from make_affines import make_affines

from tasks import *

gs = goslate.Goslate()

print len(des),len(filenames)

# Create your views here.
def home(request):
        return render(request, 'index.html', {})

@csrf_exempt        
def imgtotxt(request):
	langs = {'English':'en','Bangla':'bn','Gujarati':'gu','Hindi':'hi','Kannada':'kn','Tamil':'ta','Urdu':'ur','Telugu':'te'}
	if request.method == 'POST':
		image = request.FILES['image']
		lang = request.POST['lang']
		im = Image()
		im.image.save(image.name, image)
		im.save()
		img = cv2.imread(im.image.path,1)
		matches = getTxt(img)
		matches = sorted(matches, key=operator.itemgetter(1), reverse=True)
                matchCount = {}
                for i in frequency.keys():
                        matchCount[i] = 0
                for m in matches:
                        matchCount[int(m[0])] = matchCount[int(m[0])] + m[1]
                for k,v in frequency.iteritems():
                        matchCount[k] = matchCount[k]/v
                matchCount = sorted(matchCount.items(), key=operator.itemgetter(1), reverse=True)
		clas = matchCount[0][0]
		print 'class',clas
		image_annotation = Annotation.objects.get(image_class=clas)
		print image_annotation.image_class
		im.image_class = image_annotation.image_class
		im.save()
		text = image_annotation.text
		# Delayed the affines part :)
		make_affines.delay(im.image.path,im.image_class,text)
		if lang != 'English':
			text = gs.translate(text, langs[lang])
			print langs[lang]
			print text
		json_data = unicode(json.dumps(text), 'utf-8')
	else:
		json_data = json.dumps(['Bad Request'])
	return HttpResponse(json_data, content_type="application/json;charset=utf-8;")


def getTxt(image):
	goodMatches = []
        orb = cv2.ORB()
        kp1, des1 = orb.detectAndCompute(image,None)
        
        FLANN_INDEX_LSH = 6
        index_params= dict(algorithm = FLANN_INDEX_LSH,
                           table_number = 6, # 12
                           key_size = 12,     # 20
                           multi_probe_level = 1) #2
        search_params = dict(checks=200)
        flann = cv2.FlannBasedMatcher(index_params,search_params)
        nummatch = -1
        matchindex = -1
        print len(des)
        for j in range(0,len(des)):
                matches = flann.knnMatch(des1,des[j],k=2)
                good = 0
                if len(matches)>=2:
                        for mat in matches:
				if(len(mat))==2:
                                	m = mat[0]
					n = mat[1]
                                        if m.distance < 0.70*n.distance:
                                               	good+=1
		clas = Image.objects.all()[j]
		goodMatches.append((clas.image_class, float(good)/float(len(des))))
        
        return goodMatches

def test(request):
	langs = {'English':'en','Bangla':'bn','Gujarati':'gu','Hindi':'hi','Kannada':'kn','Tamil':'ta','Urdu':'ur','Telugu':'te'}
	if request.method == 'POST':
                image = request.FILES['image']
		lang = request.POST['lang']
                path = default_storage.save('tmp/temp.jpg', ContentFile(image.read()))
                tmp_file = os.path.join(settings.MEDIA_ROOT, path)
                img = cv2.imread(tmp_file,1)
                ind = getTxt(img)
                images = Image.objects.all()
                text = images[ind].text
		current_class = images[ind].image_class
		im = Image(image=image,image_class=current_class,text=text)
		im.save()
		image_path = im.image.path
		make_affines(image_path)
		image_name = image_path.split('.')[0]
		image_ext = image_path.split('.')[1]
		for i in range(0,8):
			im_aff = Image(image=image_name + "_" + str(i) + '.' + image_ext,image_class=current_class,text=text)
			im_aff.save()
		if lang != 'English':
			text = gs.translate(text, langs[lang])
		print text
                json_data = unicode(json.dumps(text), 'utf-8')
        	return HttpResponse(json_data, content_type="application/json;charset=utf-8;")	
	else:
			form = DocumentForm()

	return render_to_response(
			'test.html',
			{'form': form,},
			context_instance = RequestContext(request))

@csrf_exempt
def upload(request):
	langs = {'English':'en','Bangla':'bn','Gujarati':'gu','Hindi':'hi','Kannada':'kn','Tamil':'ta','Urdu':'ur','Telugu':'te'}
	if request.method == 'POST':
                image = request.FILES['image']
		lang = request.POST['lang']
		text = request.POST['text']
		image_class = request.POST['image_class']
                path = default_storage.save('tmp/temp.jpg', ContentFile(image.read()))
                tmp_file = os.path.join(settings.MEDIA_ROOT, path)
                img = cv2.imread(tmp_file,1)
                images = Image.objects.all()
		im = Image(image=image,image_class=image_class,text=text)
		im.save()
		image_path = im.image.path
		make_affines(image_path)
		image_name = image_path.split('.')[0]
		image_ext = image_path.split('.')[1]
		for i in range(0,8):
			im_aff = Image(image=image_name + "_" + str(i) + '.' + image_ext,image_class=image_class,text=text)
			im_aff.save()
		if lang != 'English':
			text = gs.translate(text, langs[lang])
		print text
                json_data = unicode(json.dumps(text), 'utf-8')
        	return HttpResponse(json_data, content_type="application/json;charset=utf-8;")	
	else:
			form = DocumentForm()

	return render_to_response(
			'test.html',
			{'form': form,},
			context_instance = RequestContext(request))

def showAddImageForm(request):
	return render_to_response('sceneText/upload_image.html')

@csrf_exempt
def upload_image(request):
	image = request.FILES['image']
	image_class = request.POST['image_class']
	image_text = request.POST['image_text']
	im_db = Image(image=image,image_class=image_class,text=image_text)
	im_db.save()
	current_class = image_class
	image_path = im_db.image.url
	image_path = os.getcwd() + image_path # Please Don't kill me for this. I hate os.path.join, didn't work
	make_affines(image_path)
	image_path = re.sub(r".jpg",'',image_path)
	im1 = Image(image=image_path + "_0" +".jpg",image_class=current_class,text=text)
	im2 = Image(image=image_path + "_1" +".jpg",image_class=current_class,text=text)
	im3 = Image(image=image_path + "_2" +".jpg",image_class=current_class,text=text)
	im4 = Image(image=image_path + "_3" +".jpg",image_class=current_class,text=text)
	im5 = Image(image=image_path + "_4" +".jpg",image_class=current_class,text=text)
	im6 = Image(image=image_path + "_5" +".jpg",image_class=current_class,text=text)
	im7 = Image(image=image_path + "_6" +".jpg",image_class=current_class,text=text)
	im8 = Image(image=image_path + "_7" +".jpg",image_class=current_class,text=text)
	im1.save()
	im2.save()
	im3.save()
	im4.save()
	im5.save()
	im6.save()
	im7.save()
	im8.save()
	return HttpResponse("OK")

	
