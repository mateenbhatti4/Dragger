from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    image = models.ImageField(null=True)


class BootstrapClasses(models.Model):
    class_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    custom = models.BooleanField(default=False)
    class_body = models.CharField(max_length=1024, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class Payments(models.Model):
    user_id = models.CharField(max_length=10)
    price = models.CharField(max_length=20,default=None,blank=True)
    current_plan = models.CharField(max_length=50,default=None)
    is_active = models.BooleanField(default=False)
