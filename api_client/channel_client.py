from .base import BaseAPIClient
from model import Channel


class ChannelClient(BaseAPIClient):
    model_class = Channel

    class Channel:
        def __init__(self, id, name, chat_id, link=None):
            self.id = id
            self.name = name
            self.chat_id = chat_id
            self.link = link

        def __repr__(self):
            return f"<Channel {self.name}>"

    def _to_obj(self, channel: Channel):
        return self.Channel(
            id=channel.id,
            name=channel.name,
            chat_id=channel.chat_id,
            link=channel.link
        )

    def is_Allowed_id(self, chat_id) -> bool:
        channels = Channel.filter(chat_id=chat_id)
        return len(channels) > 0

    def create_channel(self, name, chat_id, link) -> Channel:
        channel = Channel(id=None, name=name, chat_id=chat_id, link=link)
        channel.save()
        return self._to_obj(channel)

    def get_all(self) -> list[Channel]:
        return [self._to_obj(c) for c in Channel.get_all()]

    def get_channel_by_id(self, id) -> Channel:
        results = Channel.filter(id=id)
        if results:
            return self._to_obj(results[0])
        raise LookupError(f"Channel with id={id} not found")

    def delete_channel(self, id):
        results = Channel.filter(id=id)
        if results:
            results[0].delete()
        else:
            raise LookupError(f"Channel with id={id} not found")
