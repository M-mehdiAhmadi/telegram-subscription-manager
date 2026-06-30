from .base import BaseAPIClient
from model import Payment
import datetime


class PaymentClient(BaseAPIClient):
    model_class = Payment

    class Payment:
        def __init__(self, id, user, subscriptions, invoice_id, invoice_link, date, Completed=False):
            self.id = id
            self.user = user
            self.subscriptions = subscriptions
            self.invoice_id = invoice_id
            self.invoice_link = invoice_link
            self.date = date
            self.Completed = Completed

        def save(self):
            client = PaymentClient()
            results = Payment.filter(id=self.id)
            if results:
                payment = results[0]
                payment.invoice_id = self.invoice_id
                payment.invoice_link = self.invoice_link
                payment.save()

        def __repr__(self):
            return f"<Payment {self.id}>"

    def _to_obj(self, payment: Payment):
        return self.Payment(
            id=payment.id,
            user=payment.user,
            subscriptions=payment.subscriptions,
            invoice_id=payment.invoice_id,
            invoice_link=payment.invoice_link,
            date=payment.date,
            Completed=False  # در model فعلی Completed نداریم، بعداً اضافه می‌شود
        )

    def get_payment_by_id(self, id) -> Payment:
        results = Payment.filter(id=id)
        if results:
            return self._to_obj(results[0])
        raise LookupError(f"Payment with id={id} not found")

    def create_payment(self, user, subscriptions, invoice_id=None, invoice_link=None, date=None, Completed=False) -> Payment:
        if date is None:
            date = str(datetime.datetime.now())
        payment = Payment(
            id=None,
            user=user,
            subscriptions=subscriptions,
            invoice_id=invoice_id,
            invoice_link=invoice_link,
            date=date
        )
        payment.save()
        return self._to_obj(payment)
