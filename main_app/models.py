from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER = [
        ('m', 'male'),
        ('f', 'female'),
    ]
    CITIES = [
        ('j', 'Jedda'),
        ('r', 'Riyadh'),
        ('m', 'Macca'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_lawyer = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER, default=GENDER[0][0])
    city = models.CharField(max_length=1, choices=CITIES, default=CITIES[0][0])

    def __str__(self):
        return self.city


class Case(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cases')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='open')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Case #{self.id} - {self.title}"


class Message(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=150)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} on Case #{self.case.id}"
