#api serializers.py
from rest_framework import serializers
from  django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    id= serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields=['id','username','email','name','isAdmin']

    def get_name(self,obj):
        name = obj.first_name
        if name=='':
            name=obj.email
        return name
    def get_id(self,obj):
        
        return obj.id
    def get_isAdmin(self,obj):
        return obj.is_staff

class UserSerializerWithToken(UserSerializer):
    access = serializers.SerializerMethodField(read_only=True)
    class Meta :
        model = User
        fields=['id','username','email','name','isAdmin','access']

    def get_access(self,obj):
        access= RefreshToken.for_user(obj)
        return str(access.access_token)





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add custom claims to the response data
        data['username'] = self.user.username
        data['message'] = 'hello world'
        print(self.user.username)
        print('hello')
        return data
