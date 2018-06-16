from django.db import models
from django.contrib.auth.models import User
# from tinymce import HTMLField
from django.db.models import Sum
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from imagekit.processors import ResizeToFill
# from imagekit.models import ImageSpecField

# Create your models here.

class Profile(models.Model):
    """
    Profile class that defines objects of each profile
    """
    username = models.CharField(max_length=30,default='User')
    profile_photo = models.ImageField(upload_to="images/",null = True)
    bio = models.TextField(default='User does Not have a Bio yet',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True )
    
    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def find_profile(cls,name):
        found_profiles = cls.objects.filter(username__icontains = name).all()
        return found_profiles



