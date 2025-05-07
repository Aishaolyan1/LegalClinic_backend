from django.contrib import admin
from .models import Case, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Case)