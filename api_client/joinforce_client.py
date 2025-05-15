from .base import BaseAPIClient

class JoinforceClient(BaseAPIClient):
    class Joinforce:
        def __init__(self,id,name,link):
            self.id=id
            self.name = name
            self.link = link
    
    def __init__(self):
        # از مسیر /v1/api/joinforce/ استفاده می‌کند
        super().__init__("v1/api/joinforce/")

    def get_all(self) -> list[Joinforce]:
        force_channels = self.list()
        return [self.Joinforce(**kwargs) for kwargs in force_channels]
    
    def get_channel_by_id(self,id):
        obj = self.retrieve(obj_id=id)
        if obj:
            return self.Joinforce(**obj)
        raise LookupError("Creation Error")
    
    def create_joinforce(self,name,link) -> Joinforce :
        data = {
            "name" : name,
            "link" : link
        }
        joinforce = self.create(data=data)
        if joinforce:
            return self.Joinforce(**joinforce)
        raise LookupError("createion error")
     