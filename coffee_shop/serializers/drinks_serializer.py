from rest_framework import serializers
from ..models import Drinks  # Import from __init__.py

class DrinksSerializer (serializers.ModelSerializer):
     class Meta:
         model = Drinks
         fields = '__all__'