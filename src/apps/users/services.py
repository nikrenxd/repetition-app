import logging

from django.db import DatabaseError

from src.apps.users.models import User

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
