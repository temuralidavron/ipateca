from django.shortcuts import render
from rest_framework import generics

from page.models import House, Client
from page.serializers import HouseSerializer, ClientSerializer


class HomeView(generics.ListCreateAPIView):
    serializer_class = HouseSerializer

    def get_queryset(self):
        return House.objects.all()


class ClientView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()




