# Django and Python API Implementation Guide

## Step-by-Step Project Setup

### 1. Create a New Project Folder
Create a folder and open it in **VS Code** or your preferred IDE.

### 2. Create a Virtual Environment
Set up a virtual environment for server requirements and dependencies.
```sh
python3 -m venv .venv
```

### 3. Activate the Virtual Environment
```sh
# For Linux/Mac
source .venv/bin/activate  

# For Windows
.venv\Scripts\activate  
```

### 4. Install Django and Django REST Framework
```sh
pip install django
pip install djangorestframework
```

### 5. Verify Django Installation
```sh
django-admin --version
```

### 6. Create a Django Project
```sh
django-admin startproject myproject .
```

## Running and Checking the Server

### 7. Run the Server
```sh
python manage.py runserver
```

### 8. Handle Migration Issues
```sh
python manage.py migrate
```

### 9. Create a Superuser for Admin Panel
```sh
python manage.py createsuperuser
```
Follow the prompts:
- **Username:** admin  
- **Password:** (choose a secure one)  

### 10. Access Admin Panel
Visit: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the created credentials.

## Creating and Registering a Django App

### 11. Create a Django App
```sh
python manage.py startapp myapi
```

### 12. Register the App in `settings.py`
Add `myapi` to the `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapi',
]
```

## Creating Models and Applying Migrations

### 13. Create Models (`myapi/models.py`)
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
```

### 14. Make and Apply Migrations
```sh
python manage.py makemigrations myapi
python manage.py migrate
```

## Registering Models in Admin Panel

### 15. Register Model (`myapi/admin.py`)
```python
from django.contrib import admin
from .models import Item

admin.site.register(Item)
```

### 16. Restart the Server
```sh
python manage.py runserver
```

## Creating API Endpoints

### 17. Create a Serializer (`myapi/serializers.py`)
```python
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
```

### 18. Create API Views (`myapi/views.py`)
```python
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Override the list method to customize the response
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"drinks": serializer.data})
    
# Override the create method to customize the response
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Drink created successfully!", "drink": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Override the retreive method to customize the response
    def retreive(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Override the update method to customize the response
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Will be False for full updates
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Override the partial_update method to customize the response  
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # Ensures only provided fields are updated
        return self.update(request, *args, **kwargs)
    
# Override the destroy method to customize the response  
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Drink deleted successfully!"}, 
                        status=status.HTTP_204_NO_CONTENT)
```

### 19. Configure URLs (`myapi/urls.py`)
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### 20. Update Main URL Configuration (`myproject/urls.py`)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapi.urls')),
]
```

## Testing the API

### 21. Run the Server
```sh
python manage.py runserver
```

### 22. Test API Endpoints
- **List/Create Items:** [http://127.0.0.1:8000/api/items/](http://127.0.0.1:8000/api/items/)
- **Retrieve/Update/Delete Item:** [http://127.0.0.1:8000/api/items/<id>/](http://127.0.0.1:8000/api/items/<id>/)

## Conclusion
This document outlines the complete process of setting up a **Django project** with **Django REST Framework (DRF)** for API implementation. It includes:
- **Project setup**
- **Model creation**
- **Admin panel registration**
- **API endpoint configuration**

This guide provides a step-by-step **practical implementation** for creating and testing APIs in Django.

---

✅ **Now your API is ready to use! 🚀**

