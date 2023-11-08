from rest_framework import generics
from web.models import User, Note
from web.serializers import UserSerializer, NoteSerializer
from django.shortcuts import render


# Create your views here.
class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteAPIView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
