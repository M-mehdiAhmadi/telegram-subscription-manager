from .base import BaseAPIClient


class ChannelClient(BaseAPIClient):
    class Channel:
        id = None
        name = None
        chat_id = None
        link = None

        def __init__(self,id, name, chat_id, link):
            self.id=id
            self.name = name
            self.chat_id = chat_id
            self.link = link

    def __init__(self):
        # از مسیر /v1/api/channels/ استفاده می‌کند
        super().__init__("v1/api/channels/")

    def is_Allowed_id(self, chat_id):
        channels = self.filter(chat_id=chat_id)
        if channels:
            return True
        return False

    def create_channel(self, name, chat_id, link):
        data = {
            "name" : name,
            "chat_id" : chat_id,
            "link" : link
        }
        channel = self.create(data=data)
        if channel:
            return self.Channel(**channel)
        raise LookupError("createion error")
    def get_all(self) ->list[Channel] :
        return [ self.Channel(**channel) for channel in self.list() ]
    
    def get_channel_by_id(self,id) -> Channel :
        obj = self.retrieve(obj_id=id)
        if obj:
            return self.Channel(**obj)
        raise LookupError("createion Error")