from handlers import *
from api_client.channel_client import ChannelClient


class AllowedChannelFilter(filters.BaseFilter):

    def filter(self, message: Message) -> bool:
        """
        Check if the message is from an allowed channel.
        """
        chat_id = message.chat.id
        client = ChannelClient()
        
        return client.is_Allowed_id(chat_id=chat_id) 