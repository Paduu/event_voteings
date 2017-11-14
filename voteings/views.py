from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from voteings.models import Event, Game, Voteing
from voteings.serializers import EventSerializer, GameSerializer, VoteingSerializer, UserSerializer
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-createdDate')
    serializer_class = EventSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-createdDate')
    serializer_class = GameSerializer

class VoteingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Voteing.objects.all()
    serializer_class = VoteingSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
