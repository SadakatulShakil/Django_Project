from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, viewsets
from ..serializers import UserRegistrationSerializer, UserLoginSerializer
from ..models import Users  # Import from __init__.py

#------------------------USER------------------------#
    
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
            user = serializer.validated_data  # This is the user returned from the serializer
            
            # Serialize the user information to return in the response
            user_data = {
                "id": user.id,
                "mobile": user.mobile,
                "username": user.name,
                "profession": user.profession
                # Add any other fields you want to return
            }
            return Response({'message': 'Login successful.', "user": user_data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    