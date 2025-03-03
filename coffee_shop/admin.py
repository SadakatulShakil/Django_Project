from django.contrib import admin 
from .models import Drinks, Users, Reports  # Import from __init__.py

# register the drinks to django admin site
admin.site.register(Drinks)

# register the users to django admin site
admin.site.register(Users)

# register the report to django admin site
admin.site.register(Reports)