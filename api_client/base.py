from model import BaseModel


class BaseAPIClient:
    """
    Base class for all API clients.
    Instead of HTTP requests, directly uses the SQLite ORM (model.py).
    """
    model_class = None  # Each subclass sets this to the corresponding model

    def list(self):
        return self.model_class.get_all()

    def retrieve(self, obj_id):
        results = self.model_class.filter(id=obj_id)
        return results[0] if results else None

    def create(self, **kwargs):
        obj = self.model_class(**kwargs)
        obj.save()
        return obj

    def update(self, obj):
        obj.save()
        return obj

    def delete(self, obj):
        obj.delete()

    def filter(self, **kwargs):
        return self.model_class.filter(**kwargs)
