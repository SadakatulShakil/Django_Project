from ..models import Drinks  # Import from __init__.py
from django.http import JsonResponse
from ..serializers import DrinksSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

#----------------------DRINKS-------------------_#

class DrinksViewSet(viewsets.ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer    
    
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