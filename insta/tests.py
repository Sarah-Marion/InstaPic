from django.test import TestCase
from . models import Image, Profile, Comment, Like

# Create your tests here.
class ProfileTestClass(TestCase):
    """
    class that test the characteristics of the Profile model
    """
    def test_instance(self):
        """
        method that tests if profile objects are instantiated correctly
        """
        self.assertTrue(isinstance(self.profile,Profile))

    def setUp(self):
        """
        method that runs at the begginning of each test
        """
        self.profile = Profile(profile_photo ='test_profile_photo', bio = 'test_bio')

    def tearDown(self):
        Profile.objects.all().delete()

    def test_save_profile(self):
        """
        method that tests save method of the Profile model
        """
        self.profile.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles)>0)

        
    def test_delete_profile(self):
        """
        method that tests the delete_profile method
        """
        self.profile.save_profile()
        profile2 = Profile(profile_photo ='test_profile_photo2',bio = 'test_bio2')
        profile2.save_profile()
        self.profile.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles)==1)

    def test_find_profile(self):
        """
        method that tests the find_profile method
        """
        self.profile.save_profile()
        profile2 = Profile(profile_photo ='test_profile_photo2',bio = 'test_bio2')
        profile2.save_profile()
        search_profile = Profile.find_profile('test_bio2')
        self.assertFalse(len(search_profile)==1)


class ImageTestClass(TestCase):
    """
    A class that tests the Image class model
    """
    def test_instance(self):
        """
        method that tests if image objects are instantiated correctly
        """
        self.assertTrue(isinstance(self.image,Image)) 

    def setUp(self):
        """
        method that runs at the begginning of each test
        """
        self.image = Image(image = 'image_url',image_name ='vin' , image_caption='hey there',)

    def tearDown(self):
        Image.objects.all().delete()
   
    def test_save_image(self):
        """
        method that tests the save method of model image
        """
        self.image.save_image()
        all_images= Image.objects.all()
        self.assertTrue(len(all_images)>0)

    def test_delete_images(self):
        """
        method that tests the delete_images method
        """
        self.image.save_image()
        new_image = Image(image = 'image_url2',image_name ='vin2' , image_caption='hey there2',)
        new_image.save_image()
        self.image.delete_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images)==1)

    def test_update_caption(self):
        """
        method that tests the update caption
        """
        self.image.save_image()
        image = Image.objects.get(image ='image_url')
        image.update_caption('new caption')
        image = Image.objects.get(image ='image_url')
        self.assertTrue(image.image_caption=='new caption')

    def test_get_image_by_id(self):
        """
        method that tests the get image by id function of image model
        """
        pass
        # found_img = self.image_test.get_image_by_id(self.image_test.id)
        # img = Image.objects.filter(id=self.image_test.id)
        # self.assertTrue(found_img,img)


