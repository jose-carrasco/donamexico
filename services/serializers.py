from django.contrib.auth.models import User, Group
from services.models import Location, Type, Card
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('title', 'info', 'publish_date')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'details', 'publish_date')


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('title', 'info', 'type', 'location', 'link', 'publish_date')
