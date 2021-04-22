from django.test import TestCase
from django.test import Client
from ride.models import ride
from ride.views import *
from ride.urls import *
from authentication.views import *
from authentication.urls import *
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your tests here.

class Testviews(TestCase):    


    def setUp(self):
        client = Client()
        self.creat_url = reverse('creatride')
        self.serchride_url = reverse('serchride')
        self.profilepage_url = reverse('profilepage')
        self.contactus_url = reverse('contactus')
        self.aboutus_url = reverse('aboutus')
        self.registration_url = reverse('register')
        self.home_urls = reverse('home')
        

    def testcreatride(self):
        
        response = self.client.get(self.creat_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'creatride.html')

    
    def testserchride(self):

        response = self.client.get(self.serchride_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'serchride.html')
    
    
    def testcontactus(self):

        response = self.client.get(self.contactus_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'contactus.html')

    def testaboutus(self):

        response = self.client.get(self.aboutus_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'aboutus.html')

    def testhome(self):
        response = self.client.get(self.home_urls)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')
    