from handlers.callbackquery import *



class BuySubscriptionsHandler(BaseHandler):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True
        self.fallback_to_delete = True

    async def get(self):
        await self.show_pannel()
        await self.update.callback_query.answer()

    async def get_keyboard(self):
        subscription_id = self.update.callback_query.data.split(":")[1]
        
        subscription = Subscriptions.filter(id = subscription_id)
        if subscription:
            subscription = subscription[0] 
        else:
            raise ValueError(f"subscriptions_id:{subscription_id} is not exist")
        
        
        
        
        replay_markup = None

        keyboard = [
            [
                InlineKeyboardButton(text=f"{subscription.price}",callback_data=f"select_currency:{subscription.id}")
            ]
        ]
        
        replay_markup = InlineKeyboardMarkup(keyboard)

        return replay_markup