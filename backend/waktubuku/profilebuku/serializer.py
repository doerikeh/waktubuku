from rest_framework import serializers
from .models import ProfileWBModel, UserModel


class UserModelSerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "email", "username", "first_name", "last_name")

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