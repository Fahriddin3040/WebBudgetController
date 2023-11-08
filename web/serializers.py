from rest_framework import serializers
from web.models import User, Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('f_name', 'l_name', 'category')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'user_id', 'sort', 'reason', 'price')
