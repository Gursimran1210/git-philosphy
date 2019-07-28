from rest_framework import serializers
from .models import Words


class WordsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)
    frequency = serializers.IntegerField(read_only=True)
    word_length = serializers.IntegerField(read_only=True)
