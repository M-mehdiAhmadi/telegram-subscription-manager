from .base import BaseAPIClient

class SpecialUserClient(BaseAPIClient):

    class SpecialUser:
        def __init__(self,
                     id,
                     user ,
                    channel):
            self.id=id
            self.user = user
            self.channel = channel
            

        def __repr__(self):
            return f"<User {self.user}>"

    def __init__(self):
        # این کلاینت از مسیر /core/user/users/ استفاده می‌کند
        super().__init__("v1/api/specialusers/")

    def filter_by_username(self, username):
        lst = self.filter(user__username=username)
        if not lst:
            return None
        special_users = [self.SpecialUser(**special_user) for special_user in lst ]
        return special_users
        
    
    def create_special_user(self, user, channel) -> SpecialUser :
        data = {
            "user":user,
            "channel":channel
        }
        obj = self.create(data=data)
        if obj:
            return self.SpecialUser(**obj)
        raise LookupError("createion Error")
        