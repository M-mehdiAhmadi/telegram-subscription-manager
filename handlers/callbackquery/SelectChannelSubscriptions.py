from handlers.callbackquery import *


class SelectChannelSubscriptionsHandler(BaseHanler):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True
        self.fallback_to_delete = True

    async def get(self):
        await self.show_pannel()
        await self.update.callback_query.answer()

    def get_keyboard(self):
        channels = Channel.get_all()
        replay_markup = None

        keyboard = []
        for channel in channels:
            keyboard.append(
                    [InlineKeyboardButton(
                        text=channel.name,callback_data = f"channel_id:{channel.id}"
                )])
        replay_markup = InlineKeyboardMarkup(keyboard)

        return replay_markup
