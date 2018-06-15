from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.db.models import Sum
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from imagekit.processors import ResizeToFill
# from imagekit.models import ImageSpecField

# Create your models here.
class Image(models.Model):
    """
    Image class to define Image Objects
    """
    image = models.ImageField(upload_to='images/', verbose_name="Select Pic", null=True)
    image_name = models.CharField(max_length=30, verbose_name='Photo Name', null=True)
    image_caption = models.TextField(max_length=250, blank=True, verbose_name='Caption', null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    image_created_by = models.ForeignKey('Profile', vebose_name='Created by', related_name='owner')
    image_likes = models.ManyToManyField('Profile', related_name='Likes', blank=True, default=False)
    image_comments = models.ManyToManyField('Profile', through='Comment', through_fields=('comment_owner', 'comment_image') default=False)


    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()







    