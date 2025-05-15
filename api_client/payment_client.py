from .base import BaseAPIClient

class PaymentClient(BaseAPIClient):

    class Payment:
        def __init__(self, id, user, subscriptions, invoice_id, invoice_link, date, Completed):
            self.id = id
            self.user = user
            self.subscriptions = subscriptions
            self.invoice_id = invoice_id
            self.invoice_link = invoice_link
            self.date = date
            self.Completed = Completed

        def save(self):
            # برای ذخیره آپدیت در API
            client = PaymentClient()
            data = {
                "invoice_id": self.invoice_id,
                "invoice_link": self.invoice_link,
                "Completed": self.Completed
            }
            client.update(self.id, data)

    def __init__(self):
        super().__init__("v1/api/payments/")

    def get_payment_by_id(self,id) -> Payment :
        obj = self.retrieve(obj_id=id)
        if obj:
            return self.Payment(**obj)
        raise LookupError("creaeteion error")

    def create_payment(self, user, subscriptions, invoice_id=None, invoice_link=None, date=None, Completed=False) -> Payment:
        data = {
            "user": user,
            "subscriptions": subscriptions,
            "invoice_id": invoice_id,
            "invoice_link": invoice_link,
            "date": date,
            "Completed": Completed
        }
        obj = self.create(data=data)
        if obj:
            return self.Payment(**obj)
        raise LookupError("creation Error")
