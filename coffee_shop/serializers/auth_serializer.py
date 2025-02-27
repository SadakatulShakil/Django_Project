from rest_framework import serializers
from ..models import Users  # Import from __init__.py
from django.contrib.auth.hashers import check_password
    
    
class UserRegistrationSerializer (serializers.ModelSerializer):
     class Meta:
         model = Users
         fields = '__all__'
         extra_kwargs = {'password': {'write_only': True}} # this is use for not providing password when need user data
         
         
    # validate serialize mobile number
def validate_mobile(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("Mobile number must be 11 digits.")
        return value

    # validate serialize password
def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 digits.")
        return value
    
    # create users
def create(self, validated_data):
        user = Users.objects.create(**validated_data)
        return user
    
    # create users
class UserLoginSerializer (serializers.Serializer):
    mobile = serializers.CharField()
    password = serializers.CharField()
     
    def validate(self, data):
        mobile = data.get('mobile')
        password = data.get('password')
        
        # check if the mobile and password field is empty
        if not mobile or not password:
            raise serializers.ValidationError("Mobile number and Password Both are Required")
        
        # check the database if the user exist and the password also match
        user = Users.objects.filter(mobile=mobile).first()
        if not user or not check_password(password, user.password): #check the hash password from database
            raise serializers.ValidationError("Invalid mobile number or password.")
        
        return user