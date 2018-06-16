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


        
class Image(models.Model):
    """
    Image class to define Image Objects
    """
    image = models.ImageField(upload_to="images/",null = True )
    image_name = models.CharField(max_length =30,null = True ) 
    image_caption = models.TextField(null = True )
    pub_date = models.DateTimeField(auto_now_add=True, null= True)
    profile_key = models.ForeignKey(Profile,on_delete=models.CASCADE, null = True)
    user_key = models.ForeignKey(User,on_delete= models.CASCADE , null = True)
    likes = models.PositiveIntegerField(default=0)
    comments_number = models.PositiveIntegerField(default=0)
        
    def __str__(self):
        return self.image_name 

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete() 

    def update_caption(self,new_caption):
        self.image_caption = new_caption
        self.save()

    @classmethod
    def get_image_by_id(cls,id):
        retrived_image = Image.objects.get(id = id)
        return retrived_image

    @classmethod
    def get_images_by_user(cls,id):
        posted_images = Image.objects.filter(user_id=id)
        return posted_images

    class Meta:
        """
        Ordering of posts with the most recent showing from the top most
        """
        ordering = ['-pub_date']

    @classmethod
    def get_all_images(cls):
        all_posted_images = cls.objects.all()
        return all_posted_images 

    @classmethod
    def get_timeline_posts(cls):
        """
        A Function to get all posts of people that the current user follows
        """
        timeline_posts = Image.objects.filter()



