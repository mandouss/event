from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone
from django.forms import ModelForm


from django import forms

from django.forms.widgets import CheckboxSelectMultiple, Select

class User(AbstractUser):
    nickname = models.CharField(max_length=254, blank=True)
    #user = models.OneToOneField(User)
    class Meta(AbstractUser.Meta):
        pass
 
    def __str__(self):
        return self.username
    
    def isOwnerOf(self):
        return Event.objects.has_owner(self)
    
    def isVendorOf(self):
        return Event.objects.has_vendor(self)
    
    def isGuestOf(self):
        return Event.objects.has_guest(self)
    
    def createEvent(self, eventName, dateTime):
        newEvent = Event.objects.create_event(eventName, dateTime)
        newEvent.save()
        newEvent.addOwner(self)

class Event(models.Model):
    event_name = models.CharField(max_length = 100)
    event_detail = models.CharField(max_length = 254)
    start_time = models.DateTimeField(default = timezone.now, blank = False)
    end_time = models.DateTimeField(default = timezone.now, blank = False)
    owners = models.ManyToManyField(User, related_name = "owners")
    vendors = models.ManyToManyField(User, related_name="vendors")
    guests = models.ManyToManyField(User, related_name="guests")
    def __str__(self):
        return self.event_name
    
    def addOwner(self, user):
        self.owners.add(user)
        
    def addVendor(self, user):
        self.vendors.add(user)
        
    def addGuest(self, user):
        self.guests.add(user)
        
    def getOwners(self):
        return self.owners.all()
    
    def getVendors(self):
        return self.vendors.all()
    
    def getGuests(self):
        return self.guests.all()

# Create your models here.
