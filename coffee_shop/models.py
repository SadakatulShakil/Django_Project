from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# create the model here
class Drinks(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=20)

    # design the object  (how its looking in django admin)
    def __str__(self):
        return self.name+ ' ->'+' remaining: '+ self.stock +' ('+self.price+')'
    
    
    
# create the user here
class Users(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15,
                              unique=True,
                              validators=[
            RegexValidator(
                regex=r'^\d{11}$',  # Ensures exactly 11 digits
                message='Mobile number must be exactly 11 digits.',
            )
        ])
    profession = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    
    # secure the password
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)  # Hash the password
        super().save(*args, **kwargs)
    
    #condition apply here
    def clean(self):
        if len(self.mobile) != 11:
            raise ValidationError({'mobile': 'Mobile number must be 11/14 digits.'})
        if len(self.password) < 6:
            raise ValidationError({'password': 'Password must be at least 6 digits.'})
        if Users.objects.filter(mobile=self.mobile).exclude(pk=self.pk).exists():
            raise ValidationError({'mobile': 'This mobile number is already registered.'})

    # design the object  (how its looking in django admin)
    def __str__(self):
        return self.name