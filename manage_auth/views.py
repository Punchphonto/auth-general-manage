
from.models import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
                {
                    'user_id': user.id,
                    'name': user.first_name,
                    'token': token.key, 
                    "is_staff":user.is_staff,
                    "success": True
                }, 
                status=status.HTTP_200_OK
            )
    
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_is_authenticate(request):
    return JsonResponse({"is_authenticate":True})