from django.db import models

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
    mobile = models.CharField(max_length=15)
    profession = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    
    #condition apply here
    def clean(self):
        if len(self.mobile) != 11:
            raise ValidationError({'mobile': 'Mobile number must be 11 digits.'})
        if len(self.password) < 6:
            raise ValidationError({'password': 'Password must be at least 6 digits.'})

    # design the object  (how its looking in django admin)
    def __str__(self):
        return self.name