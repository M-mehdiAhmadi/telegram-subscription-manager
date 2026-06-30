from .base import BaseAPIClient
from model import User
import datetime


class UserClient(BaseAPIClient):
    model_class = User

    class User:
        def __init__(self, chat_id, time_created, is_active, phone, is_admin, language, is_special=0):
            self.id = chat_id        # handlers use .id
            self.username = chat_id  # handlers use .username
            self.chat_id = chat_id
            self.time_created = time_created
            self.is_active = is_active
            self.phone = phone
            self.is_admin = is_admin
            self.language = language
            self.is_special = is_special

        def save(self):
            # client = UserClient()
            user = User(
                chat_id=self.chat_id,
                time_created=self.time_created,
                is_active=self.is_active,
                phone=self.phone,
                is_admin=self.is_admin,
                language=self.language,
                is_special=self.is_special
            )
            user.save()

        def __repr__(self):
            return f"<User {self.username}>"

    def _to_obj(self, user: User):
        return self.User(
            chat_id=user.chat_id,
            time_created=user.time_created,
            is_active=user.is_active,
            phone=user.phone,
            is_admin=user.is_admin,
            language=user.language,
            is_special=user.is_special
        )

    def getUser_by_username(self, username) -> User | None:
        user = User.get_by_chat_id(chat_id=username)
        if user:
            return self._to_obj(user)
        return None

    def create_user(self, user_data) -> User:
        user = User(
            chat_id=user_data["username"],
            time_created=str(datetime.datetime.now()),
            is_active=user_data.get("is_active", True),
            phone=user_data.get("phone", None),
            is_admin=user_data.get("is_admin", False),
            language=user_data.get("language", "en"),
            is_special=user_data.get("is_special", False)
        )
        user.save()
        return self._to_obj(user)

    def get_all_admin(self) -> list[User] | None:
        users = User.filter(is_admin=1)
        if users:
            return [self._to_obj(u) for u in users]
        return None

    def get_all_special(self) -> list[User] | None:
        users = User.filter(is_special=1)
        if users:
            return [self._to_obj(u) for u in users]
        return None
