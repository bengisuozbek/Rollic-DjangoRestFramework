from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Users
from .serializers import RollicSerializer

# Create your views here.
class RollicListApiView(APIView):

    # controlling the user is authenticated or not
    permission_classes = [permissions.IsAuthenticated]

    # All users list
    # Get all users
    def get(self, request, *args, **kwargs):
        try:
            the_users = Users.objects.all()
            if not the_users:
                return Response(
                    {"res": "User with that id does not exist"},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = RollicSerializer(the_users, many = True)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                    {"error": "Bad request"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {"error": "server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    # Creation of a new user -> sign up page
    # Add a user!
    def post(self, request, *args, **kwargs):
        try:
            data = {
                'username': request.data.get('username'),
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
                'email': request.data.get('email'),
                'phone': request.data.get('phone'),
                'password': request.data.get('password'),
                'confirm_password': request.data.get('confirm_password')
            }

            serializer = RollicSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                if Users.objects.get(mail = serializer.mail):
                    return Response(
                        {"error": "User with that email already exist"},
                        status=status.HTTP_403_FORBIDDEN
                    )
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Bad request"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {"error": "server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RollicDetailApiView(APIView):

    # controlling the user is authenticated or not
    permission_classes = [permissions.IsAuthenticated]
   
    # To control the data when getting only one User object 
    def get_object(self, user_id):
        try:
            return Users.objects.get(id = user_id)
        except Users.DoesNotExist:
            return None

    # Getting the selected user from its user_id
    # Find a user with ID
    def get(self, request, user_id, *args, **kwargs):
        try:
            user_instance = self.get_object(user_id)
            if not user_instance:
                return Response(
                    {"error": "User with that id does not exists"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = RollicSerializer(user_instance)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Bad request"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {"error": "server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Editing the user's information 
    # Edit a user's attribute
    def put(self, request, user_id, *args, **kwargs):
        try:
            user_instance = self.get_object(user_id)
            if not user_instance:
                return Response(
                    {"error": "User with that id does not exist"}, 
                    status=status.HTTP_404_NOT_FOUND
                )

            data = {
                'username': request.data.get('username'),
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
                'email': request.data.get('email'),
                'phone': request.data.get('phone'),
                'password': request.data.get('password'),
                'confirm_password': request.data.get('confirm_password')
            }

            serializer = RollicSerializer(instance = user_instance, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Bad request"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {"error": "server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Deleting the user
    # Delete a user
    def delete(self, request, user_id, *args, **kwargs):
        try:
            user_instance = self.get_object(user_id)
            if not user_instance:
                return Response(
                    {"error": "User with that id doest not exist"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            user_instance.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(
                {"error": "server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )