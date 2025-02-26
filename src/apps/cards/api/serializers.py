from rest_framework import serializers

from src.apps.cards.models import Card, CardState


class CardSerializer(serializers.ModelSerializer):
    answered = serializers.BooleanField(source="card_state.answered")

    class Meta:
        model = Card
        fields = ("id", "question", "answer", "answered")


class CardCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("question", "answer", "deck")


class CardStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardState
        fields = ("answered",)
