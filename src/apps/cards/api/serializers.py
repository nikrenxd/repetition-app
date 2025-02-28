from rest_framework import serializers

from src.apps.cards.models import Card, CardState
from src.apps.notes.api.serializers import NoteSerializer


class CardSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)
    answered = serializers.BooleanField(source="card_state.answered")

    class Meta:
        model = Card
        fields = ("id", "question", "answer", "notes", "answered")


class CardCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("question", "answer", "deck")


class CardStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardState
        fields = ("answered",)
