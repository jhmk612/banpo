from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class People(models.Model):
    name=models.CharField(max_length=20)



def upload_location(instance, filename):
    return "%s/%s" %(instance.person.name, filename)

class Post(models.Model):
    title=models.CharField(max_length=30)
    media=models.FileField(upload_to=upload_location, null=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content=models.TextField()
    person=models.ForeignKey(People, default=1)
    writer=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

class Comment(models.Model):
    post=models.ForeignKey(Post)
    content=models.TextField()
    writer=models.ForeignKey(settings.AUTH_USER_MODEL)

class Like(models.Model):
    post=models.ForeignKey(Post)
    rating=models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(10)], help_text='10점 만점, 높을수록 극혐!', blank=True, default=5)
    liker=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
