from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password', 'address'
        )


# class FbSerializer(serializers.Serializer):
#     provider = serializers.CharField(max_length=255, required=True)
#     access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)