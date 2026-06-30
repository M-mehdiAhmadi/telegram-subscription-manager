from .base import BaseAPIClient
from model import Specialuser


class SpecialUserClient(BaseAPIClient):
    model_class = Specialuser

    class SpecialUser:
        def __init__(self, id, user, channel):
            self.id = id
            self.user = user
            self.channel = channel

        def __repr__(self):
            return f"<SpecialUser {self.user}>"

    def _to_obj(self, su: Specialuser):
        return self.SpecialUser(id=su.id, user=su.user, channel=su.channel)

    def filter_by_username(self, username) -> list[SpecialUser] | None:
        results = Specialuser.filter(user=username)
        if not results:
            return None
        return [self._to_obj(su) for su in results]

    def create_special_user(self, user, channel) -> SpecialUser:
        su = Specialuser(id=None, user=user, channel=channel)
        su.save()
        return self._to_obj(su)

    def delete_special_user(self, id):
        results = Specialuser.filter(id=id)
        if results:
            results[0].delete()
        else:
            raise LookupError(f"SpecialUser with id={id} not found")
