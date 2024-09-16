from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError({'msg' : 'User already exist'})
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
                                    username = validated_data['username'], 
                                    first_name = validated_data['first_name'],
                                    last_name = validated_data['last_name'],
                                  )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    

class LoginSerilaizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if not User.objects.filter(username = username).exists():
            raise serializers.ValidationError({'msg' : 'User not found'})
        return data
        

    def get_jwt_token(self,validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')

        user = authenticate(username = username, password = password)
        if not user:
            return {'msg': 'invalid credentials'}
        refresh = RefreshToken.for_user(user)
        return  {'msg' : 'login success', 'refresh': str(refresh), 'access': str(refresh.access_token)}

        

        