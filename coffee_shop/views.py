from .models import Drinks, Users
from django.http import JsonResponse
from .serializer import DrinksSerializer, UserRegistrationSerializer, UserLoginSerializer
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

#------------------------USER------------------------#
    
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserRegistrationSerializer
    
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserRegistrationSerializer

    # Override the list method to customize the response
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"users": serializer.data})

    # Override the create method for custom registration handling
    def create(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully registered.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Override the destroy method to delete a user
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()  # Get the user object based on the provided pk (primary key)
        user.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

#------------------LOGIN------------------#

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Login successful.', "user": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
     
# ## get all Drinks Data
# @api_view(['GET'])
# def drinks_list(request):
#  # get all the drinks
#     drinks = Drinks.objects.all()
#  # serialize them
#     serializer = DrinksSerializer(drinks, many = True)
#  # return JSON to user  
#     return JsonResponse({'drinks': serializer.data})


# ## create Drinks Data
# @api_view(['POST'])
# def create_drink(request):
#  # serialize them
#     serializer = DrinksSerializer(data = request.data)
#  # check the data if it is valid
#     if serializer.is_valid():
#         # save the data if it is valid
#         serializer.save()
#          # return JSON to user  
#         return Response(serializer.data, status = status.HTTP_201_CREATED)
    

# ## get specific Drink Data
# @api_view(['GET'])
# def drink_details(request, id):
#     try:
#         drink = Drinks.objects.get(pk=id)
#         serializer = DrinksSerializer(drink)
#         return Response(serializer.data)
#     except Drinks.DoesNotExist:
#         return Response({"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND)

    
    
# ## update specific Drink Data
# @api_view(['POST'])
# def update_drink(request, id):
#     try:
#         drink = Drinks.objects.get(pk=id)
#         serializer = DrinksSerializer(drink, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data, status = status.HTTP_200_OK)
#     except Drinks.DoesNotExist:
#         return Response({"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND)


# ## remove specific Drink Data
# @api_view(['POST'])
# def remove_drink(request, id):
#     try:
#         drink = Drinks.objects.get(pk=id)
#         drink.delete()
#         return Response({"message": "Drink deleted successfully"}, status = status.HTTP_200_OK)
#     except Drinks.DoesNotExist:
#         return Response({"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND)