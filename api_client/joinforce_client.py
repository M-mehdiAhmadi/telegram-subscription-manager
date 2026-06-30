from .base import BaseAPIClient
from model import Joinforce


class JoinforceClient(BaseAPIClient):
    model_class = Joinforce

    class Joinforce:
        def __init__(self, id, name, link):
            self.id = id
            self.name = name
            self.link = link

        def __repr__(self):
            return f"<Joinforce {self.name}>"

    def _to_obj(self, jf: Joinforce):
        return self.Joinforce(id=jf.id, name=jf.name, link=jf.link)

    def get_all(self) -> list[Joinforce]:
        return [self._to_obj(jf) for jf in Joinforce.get_all()]

    def get_channel_by_id(self, id) -> Joinforce:
        results = Joinforce.filter(id=id)
        if results:
            return self._to_obj(results[0])
        raise LookupError(f"Joinforce with id={id} not found")

    def create_joinforce(self, name, link) -> Joinforce:
        jf = Joinforce(id=None, name=name, link=link)
        jf.save()
        return self._to_obj(jf)

    def delete_joinforce(self, id):
        results = Joinforce.filter(id=id)
        if results:
            results[0].delete()
        else:
            raise LookupError(f"Joinforce with id={id} not found")
