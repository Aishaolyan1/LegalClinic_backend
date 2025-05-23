from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

# User Registration
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [permissions.AllowAny]

  def create(self, request, *args, **kwargs):
    try:
      role = request.data["role"]
      gender = request.data["gender"]
      city = request.data["city"]
      del request.data["role"]
      del request.data["city"]
      del request.data["gender"]
      response = super().create(request, *args, **kwargs)
      user = User.objects.get(username=response.data['username'])
      check_lawyer = True if role == 'lawyer' else False
      profile = Profile.objects.create(user=user, is_lawyer=check_lawyer, gender=gender, city=city)
      print(profile, "check profile")
      refresh = RefreshToken.for_user(user)
      content = {'refresh': str(refresh), 'access': str(refresh.access_token), 'user': response.data, "profile": ProfileSerializer(profile).data }
      return Response(content, status=status.HTTP_200_OK)
    except (ValidationError, IntegrityError) as err:
      print(str(err), "testing user create error")
      return Response({ 'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
  permissions_classes = [permissions.AllowAny]

  def post(self, request):
    try:
      username = request.data.get('username')
      password = request.data.get('password')
      user = authenticate(username=username, password=password)
      if user:
        refresh = RefreshToken.for_user(user)
        profile = Profile.objects.get(user=user)
        content = {'refresh': str(refresh), 'access': str(refresh.access_token),'user': UserSerializer(user).data, "profile": ProfileSerializer(profile).data}
        return Response(content, status=status.HTTP_200_OK)
      return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    try:
      user = User.objects.get(username=request.user.username)
      try:
        refresh = RefreshToken.for_user(user)
        profile = Profile.objects.get(user=user)
        content = {'refresh': str(refresh), 'access': str(refresh.access_token),'user': UserSerializer(user).data, "profile": ProfileSerializer(profile).data}
        return Response(content, status=status.HTTP_200_OK)
      except Exception as token_error:
        return Response({"detail": "Failed to generate token.", "error": str(token_error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
      return Response({"detail": "Unexpected error occurred.", "error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

class LawyerCreateListView(APIView):

  def get(self, request):
    lawyers = Profile.objects.filter(is_lawyer=True)
    serialized = ProfileSerializer(lawyers, many=True)
    return Response(serialized.data)


class LawyerDetail(APIView):
  serializer_class = ProfileSerializer
  lookup_field = 'id'

  def get(self, request, lawyer_id):
    try:
      queryset = Profile.objects.get(id=lawyer_id)
      lawyer = ProfileSerializer(queryset)
      return Response(lawyer.data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def put(self, request, lawyer_id):
    try:
        lawyer = get_object_or_404(Profile, id=lawyer_id)
        serializer = self.serializer_class(lawyer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def delete(self, request, lawyer_id):
    try:
        lawyer = get_object_or_404(Profile, id=lawyer_id)
        lawyer.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
      
     
  
