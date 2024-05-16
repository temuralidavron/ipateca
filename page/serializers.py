from rest_framework import serializers

from page.models import House, Client


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'ipateca', 'quantity', 'price',)


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'phone', 'email','price','quantity','house')


    