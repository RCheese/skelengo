from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import Ship


class ShipSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ("id", "title", "tags")

    id = serializers.IntegerField()
    title = serializers.CharField()
    tags = TagListSerializerField()
