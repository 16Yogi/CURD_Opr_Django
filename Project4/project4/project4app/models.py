from django.db import models

class RegistrationForm(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)  
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    password = models.CharField(max_length=250)  

    # def __str__(self):
    #     return self.username
