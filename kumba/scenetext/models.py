from django.db import models
import pickle

# Create your models here.
class Image(models.Model):
    image = models.ImageField(
        upload_to="images/"
    )
    image_class = models.IntegerField(
        blank=False,
    	default = 0,
    )

class Annotation(models.Model):
    image_class = models.IntegerField(
		    blank = False,
		    default = 0,
		    )
    text = models.CharField(max_length=60,
        blank=True, 
        null=True
    )

with open('/home/cloudstrife/Documents/kumbathon/kumba/scenetext/orb.pickle') as f:
	des, filenames, frequency = pickle.load(f)
