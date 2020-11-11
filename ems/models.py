from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.enums import Choices


class Participant(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, choices=GENDER)
    dob = models.DateField()
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Organiser(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Event(models.Model):
    CATEGORIES = [
        ('Virtual Conference', 'Virtual Conference'),
        ('Hackathon', 'Hackathon'),
        ('Coding Contest', 'Coding Contest'),
        ('Quiz', 'Quiz'),
        ('Webinar', 'Webinar'),
        ('Product Launch', 'Product Launch'),
        ('Trade Show', 'Trade Show')
    ]
    name = models.CharField(max_length=200)
    organiser = models.ForeignKey(Organiser, null=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True)
    category = models.CharField(max_length=200, choices=CATEGORIES)
    event_date = models.DateField()
    created_dated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Transaction(models.Model):
    participant = models.ForeignKey(Participant, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return self.participant + '-' + self.event + '-' + str(self.amount)


class Cancellation(models.Model):
    participant = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    reason = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user + '-' + self.event


class Advertisement(models.Model):
    DURATIONS = [
        (2, 2),
        (6, 6),
        (12, 12),
        (24, 24),
        (48, 48)
    ]
    event = models.ForeignKey(Event, on_delete=CASCADE)
    duration = models.IntegerField(default=2, choices=DURATIONS)

    def __str__(self):
        return self.event.name

    def getEvent(self):
        return self.event


class Item(models.Model):
    CATEGORIES = [
        ('T-Shirt', 'T-Shirt'),
        ('Coffee Mug', 'Coffee Mug'),
        ('Stickers', 'Sticker'),
        ('Backpack', 'Backpack'),
    ]
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORIES)

    def __str__(self):
        return self.name


class Shipper(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Registration(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.participant.name + '-' + self.event.name


