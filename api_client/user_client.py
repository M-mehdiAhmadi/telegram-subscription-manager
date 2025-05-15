from .base import BaseAPIClient

class UserClient(BaseAPIClient):

    class User:
        def __init__(self,
                     id=None,
                     username=None,
                     is_admin=None,
                     phone=None,
                     language=None,
                     is_active=None,
                     is_special=None):
            self.id = id
            self.username = username
            self.is_admin = is_admin
            self.phone = phone
            self.language = language
            self.is_active = is_active
            self.is_special = is_special
        def save(self):
            client = UserClient()
            return client.update(self.id, {
                    "username": self.username,
                    "is_admin": self.is_admin,
                    "phone": self.phone,
                    "language": self.language,
                    "is_active": self.is_active,
                    "is_special": self.is_special,
                })

        def __repr__(self):
            return f"<User {self.username}>"

    def __init__(self):
        # این کلاینت از مسیر /core/user/users/ استفاده می‌کند
        super().__init__("core/user/users/")

    def getUser_by_username(self, username) -> User | None:
        users = self.filter(username=username)
        if users:
            return self.User(**users[0])
        return None

    def create_user(self,user_data):
        user = self.create(data=user_data)
        return self.User(**user)
    
    def get_all_admin(self):
        objs = self.filter(is_admin=True)
        if objs:
            return [self.User(**obj) for obj in objs]
        return None
    
    def get_all_special(self):
        objs = self.filter(is_special=True)
        if objs:
            return [self.User(**obj) for obj in objs]
        return None
    