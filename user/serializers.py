from rest_framework import serializers
from . models import MyUser


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('username', 'phone_number', 'password')

    def create(self, validated_data):
        user = MyUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = (
            'id',
            'username',
            'phone_number',
            'email',
            'cover',
        )


