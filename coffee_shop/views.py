from .models import Drinks
from django.http import JsonResponse
from .serializer import DrinksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


## get all Drinks Data
@api_view(['GET'])
def drinks_list(request):
 # get all the drinks
    drinks = Drinks.objects.all()
 # serialize them
    serializer = DrinksSerializer(drinks, many = True)
 # return JSON to user  
    return JsonResponse({'drinks': serializer.data})


## create Drinks Data
@api_view(['POST'])
def create_drink(request):
 # serialize them
    serializer = DrinksSerializer(data = request.data)
 # check the data if it is valid
    if serializer.is_valid():
        # save the data if it is valid
        serializer.save()
         # return JSON to user  
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    

## get specific Drink Data
@api_view(['GET'])
def drink_details(request, id):
    try:
        drink = Drinks.objects.get(pk=id)
        serializer = DrinksSerializer(drink)
        return Response(serializer.data)
    except Drinks.DoesNotExist:
        return Response({"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND)

    
    
## update specific Drink Data
@api_view(['POST'])
def update_drink(request, id):
    try:
        drink = Drinks.objects.get(pk=id)
        serializer = DrinksSerializer(drink, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    except Drinks.DoesNotExist:
        return Response({"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND)


## remove specific Drink Data
@api_view(['POST'])
def remove_drink(request, id):
    try:
        drink = Drinks.objects.get(pk=id)
        drink.delete()
        return Response({"message": "Drink deleted successfully"}, status = status.HTTP_200_OK)
    except Drinks.DoesNotExist:
        return Response({"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND)