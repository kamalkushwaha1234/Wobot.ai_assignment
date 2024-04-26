from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers import MyTokenObtainPairSerializer,UserSerializerWithToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer): 
    def validate(self, attrs):
        data = super().validate(attrs)
       
        serializer =UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k]= v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



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


def register_page(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = User.objects.filter(username=username)

        if user.exists():
            
            messages.info(request, "Username already taken!")
            return redirect('register')

        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        
        user.set_password(password)
        user.save()

        
        messages.info(request, "Account created Successfully!")
        return redirect('home')

    
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

