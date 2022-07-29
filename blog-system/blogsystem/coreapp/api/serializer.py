from rest_framework import serializers
from blog_app.models import Blog


# class ProfileSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     TYPE_SELECT = (
#         ('Female', 'Female'),
#         ('Male', 'Male'),
#     )
#     user = serializers.OneToOneField('user.User', on_delete=models.CASCADE, related_name='profile_user')
#     gender = serializers.CharField(max_length=11, choices=TYPE_SELECT)
#     dob = serializers.DateField()
#     bio = serializers.CharField(max_length=150)
#     link = serializers.URLField(max_length=100)
from coreapp.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


