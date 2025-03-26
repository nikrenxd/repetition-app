import logging

from django.db import DatabaseError

from src.apps.users.models import User, UserStatistics

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
            user_stats = UserStatistics.objects.create(user=user)
            return user_stats
        except DatabaseError as e:
            logger.error(f"Error when creating user stats: {e}")
