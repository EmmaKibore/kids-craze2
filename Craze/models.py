from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile/')


    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles



class Category(models.Model):
    image_category = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.image_category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Image(models.Model):
    
    image_path = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30, blank=False)
    category = models.ForeignKey(Category)
   
    def __str__(self):
       return self.image_name
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_image(cls, search_category):
        images = cls.objects.filter(category__image_category__icontains = search_category)
        return images

