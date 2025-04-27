from handlers.callbackquery import *



class SelectSubscriptionsHandler(BaseHanler):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True
        self.fallback_to_delete = True

    async def get(self):
        await self.show_pannel()
        await self.update.callback_query.answer()

    def get_keyboard(self):
        channel_id = self.update.callback_query.data.split(":")[1]
        
        subscriptions = Subscriptions.filter(channel = channel_id)
        replay_markup = None

        keyboard = []
        for subscription in subscriptions:
            keyboard.append(
                    [InlineKeyboardButton(
                        text=subscription.name,callback_data = f"subscription_id:{subscription.id}"
                )])
        replay_markup = InlineKeyboardMarkup(keyboard)

        return replay_markup
    