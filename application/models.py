from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Post(models.Model):
    ''' a model for Image posts '''
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    live_link = models.URLField()
    description = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def save_post(self):
        ''' method to save an image post instance '''
        self.save()

    def delete_post(self):
        '''method to delete an image post instance '''
        self.delete()

    @classmethod
    def search_project(cls, search_term):
        ''' method to search projects by title '''
        return cls.objects.filter(title__icontains=search_term).all()



class Profile(models.Model):
    ''' extended User model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True, default=f'Hello, I am new here!')

    def __str__(self):
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Rating(models.Model):
    ''' model to allow users to rate post on three categories '''
    Rating_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
    )
    interface = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    experience = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    content = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post}'s rating"

    def save_rating(self):
        ''' method to save ratings '''
        self.save()

    def delete_rating(self):
        ''' method to delete ratings '''
        self.delete()