from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Post(models.Model):
    ''' a model for Image posts '''
    image = models.ImageField(upload_to='images/')
    title = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    live_link = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def save_post(self):
        ''' method to save an image post instance '''
        self.save()

    def delete_post(self):
        '''method to delete an image post instance '''
        self.delete()


class Profile(models.Model):
    ''' extended User model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True, default=f'Hello, I am new here!')

    def __str__(self):
        return f'{self.user.username}'

    def save_profile(self):
        ''' method to save a user's profile '''
        self.save()

    def delete_profile(self):
        '''method to delete a user's profile '''
        self.delete()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Rate(models.Model):
    ''' model to allow users to rate post on three categories '''
    pass