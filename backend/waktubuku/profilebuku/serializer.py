from rest_framework import serializers
from .models import ProfileWBModel, UserModel
from django.contrib.auth import authenticate

class UserModelSerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "email", "username")
        


class ProfileSerializer(serializers.ModelSerializer):

    user = UserModelSerialier()

    class Meta:
        model = ProfileWBModel
        fields = ("id", "slug", "image_profile", "image_walpaper", "date_created",
                    "date_updated", "biografi", "alamat", "gender", "saldo","user")
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", 'email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            user = UserModel.objects.create_user(validated_data['username'], validated_data['email'],
            validated_data['password'])
            return user

class UserLogin(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("tidak cocok")