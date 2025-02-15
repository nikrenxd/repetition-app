from rest_framework import serializers

from src.apps.cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("id", "question", "answer")


class CardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("question", "answer", "deck")
