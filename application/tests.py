from django.test import TestCase
from .models import Post, Profile
from datetime import datetime
from django.contrib.auth.models import User



class ProfileTest(TestCase):
    ''' test class for Profile model'''
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='Water')

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()

    def test_profile_creation(self):
        ''' method to test profile instance is created only once for each user '''
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)
        

class TestImage(TestCase):
    ''' test class for image model '''
    def setUp(self):
        ''' method called before each test case'''
        self.test_user = User(username='Linda', password='123')
        self.test_user.save()
        self.test_profile = self.test_user.profile
        self.test_profile.save()

        self.test_post = Post(image='images/test.jpg', title='some text', profile=self.test_profile, live_link='https://www.google.com', created_on=datetime.now())

    def test_instance(self):
        ''' test method to ensure image instance creation '''
        self.assertTrue(isinstance(self.test_post, Post))

    def test_save(self):
        ''' test method to save image instance to db '''
        self.test_post.save_post()
        self.assertEqual(len(Post.objects.all()), 1)

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.test_user.delete() #deletes it's profile too
        Post.objects.all().delete()