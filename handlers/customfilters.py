from handlers import *

class AllowedChannelFilter(filters.BaseFilter):

    def filter(self, message: Message) -> bool:
        """
        Check if the message is from an allowed channel.
        """
        chat_id = message.chat.id
        allowed_ids = {channel.chat_id for channel in Channel.get_all()}
        return chat_id in allowed_ids