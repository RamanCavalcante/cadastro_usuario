from rest_framework import serializers
from registration.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name','password', 'birth_date']
        