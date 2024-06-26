from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers import MyTokenObtainPairSerializer,UserSerializerWithToken,UserSerializer
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes
from django.views.decorators.csrf import csrf_exempt



class MyTokenObtainPairSerializer(TokenObtainPairSerializer): 
    def validate(self, attrs):
        data = super().validate(attrs)
       
        serializer =UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k]= v
        Shared_data(self.context['request'],data)
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

def Shared_data(request,data):
    shared_data=data
    request.session['shared_data'] = shared_data




@csrf_exempt
def login_page(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username: ' + username + ' password: ' + password)

        if not User.objects.filter(username=username).exists():

            messages.error(request, 'Invalid Username')
            return redirect('login')

    
        user = authenticate(username=username, password=password)

        if user is None:
        
            messages.error(request, "Invalid Password")
            return redirect('login')
        else:
            
            login(request, user)
            return redirect('home')
    else:
        print('method is not post')

    
    return render(request, 'login.html')


@api_view(['POST'])
def registerUser(request):
    data=request.data
    username = data.get('email')
    print("from User_viwes user data " )
    print(data)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)
    else :
        user =User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        username=username,
        email=data['email'],
        password=make_password(data['password']))
        serializer=UserSerializerWithToken(user,many=False)
        print(serializer.data)
        shared_data=serializer.data
        request.session['shared_data']=shared_data
        return Response(serializer.data)



        
def register_page(request):
    
    
    
    return render(request, 'register.html')


@login_required
def profile_page(request):
    
    user = request.user
    context = {'user': user}
    print(context)
    return render(request, 'profile.html', context)


def logout_user(request):
    logout(request)

    return redirect('home')



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user =request.user
    serializer=UserSerializer(user)
    return Response(serializer.data)