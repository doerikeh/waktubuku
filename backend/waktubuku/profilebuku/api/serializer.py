from rest_framework import serializers
from ..models import UserModel
from django.contrib.auth import authenticate
from django.contrib.auth import user_logged_in
from phonenumber_field.serializerfields import PhoneNumberField


UserModel._meta.get_field('email')._unique = True

class UserModelSerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "email", "username_user", "no_telepon")
        

class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", 'email', 'username_user', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            validated_data['email'],
            validated_data['username_user'],
            validated_data['password'],            
        )
        return user

class UserLogin(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(request=self.context['request'], **data)
        if user and user.is_active:
            user_logged_in.send(sender=user.__class__, request=self.context['request'], user=user)
            return user
        raise serializers.ValidationError("tidak cocok")