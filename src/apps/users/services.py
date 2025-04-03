import logging

from django.db import DatabaseError
from django.db.models import Count, Q, F, FloatField, QuerySet
from django.db.models.functions import Cast, Round

from src.apps.users.models import User, UserStatistic

logger = logging.getLogger(__name__)


class UserService:
    @staticmethod
    def create_user(model: User, **data):
        try:
            user = model.objects.create_user(**data)
            logger.info("User created")
            return user
        except DatabaseError as e:
            logger.error(f"Error when creating user: {e}")

    @staticmethod
    def create_user_statistic(user: User):
        try:
            user_stats = UserStatistic.objects.create(user=user)
            return user_stats
        except DatabaseError as e:
            logger.error(f"Error when creating user stats: {e}")

    @staticmethod
    def get_user_statistic(qs: QuerySet[User]):
        try:
            statistic = (
                qs.annotate(
                    total_decks=Count("decks"),
                    completed_decks=Count("decks", filter=Q(decks__completed=True)),
                )
                .annotate(
                    completed_decks_percentage=Round(
                        Cast(F("completed_decks"), FloatField())
                        / Cast(F("total_decks"), FloatField()),
                        precision=2,
                    ),
                )
                .first()
            )

            return statistic
        except DatabaseError as e:
            logger.error(f"Error when getting user statistic: {e}")
