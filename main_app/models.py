from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_lawyer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Lawyer: {self.is_lawyer}"



class Case(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cases')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Case {self.id}: {self.title}"




class Message(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=150)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} for Case {self.case.id}"
