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