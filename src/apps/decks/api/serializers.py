from rest_framework import serializers

from src.apps.decks.models import Deck


class DeckSerializer(serializers.ModelSerializer):
    # TODO: Field for count cards in deck

    class Meta:
        model = Deck
        fields = ("id", "name", "completed")


class DeckRetrieveSerializer(serializers.ModelSerializer):
    # TODO: Field for cards in deck

    class Meta:
        model = Deck
        fields = ("name", "description")


class DeckCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ("name", "description")
