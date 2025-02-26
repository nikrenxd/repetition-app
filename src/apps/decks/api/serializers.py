from rest_framework import serializers

from src.apps.cards.api.serializers import CardSerializer
from src.apps.decks.models import Deck


class DeckSerializer(serializers.ModelSerializer):
    cards_count = serializers.SerializerMethodField(method_name="get_cards_count")

    def get_cards_count(self, deck):
        return deck.cards.count()

    class Meta:
        model = Deck
        fields = ("id", "name", "completed", "cards_count")


class DeckRetrieveSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)

    class Meta:
        model = Deck
        fields = ("name", "description", "cards")


class DeckCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ("name", "description")
