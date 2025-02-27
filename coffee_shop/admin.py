from django.contrib import admin 
from .models import Drinks, Users  # Import from __init__.py

# register the drinks to django admin site
admin.site.register(Drinks)

# register the users to django admin site
admin.site.register(Users)