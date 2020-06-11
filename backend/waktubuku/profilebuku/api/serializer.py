from rest_framework import serializers
from ..models import UserModel
from django.contrib.auth import authenticate
from django.contrib.auth import user_logged_in
from phonenumber_field.serializerfields import PhoneNumberField


UserModel._meta.get_field('email')._unique = True


class UserModelSerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "email", "username_user", "no_telepon", "slug",
         "image_walpaper", "date_updated", "biografi", "alamat", "gender", "saldo")


    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.username_user = validated_data.get("username_user", instance.username_user)
        instance.no_telepon = validated_data.get("no_telepon", instance.no_telepon)
        instance.image_walpaper = validated_data.get("image_walpaper", instance.image_walpaper)
        instance.biografi = validated_data.get("biografi", instance.biografi)
        instance.alamat = validated_data.get("alamat", instance.alamat)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.saldo = validated_data.get("saldo", instance.saldo)
        

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