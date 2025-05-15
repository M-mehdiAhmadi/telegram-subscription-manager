import requests
from .utils import handle_response

class BaseAPIClient:
    _domain = "http://127.0.0.1:8000/"
    def __init__(self, base_url:str):
        
        self.base_url = (self._domain.rstrip('/') + '/') + base_url.lstrip("/").rstrip('/') + '/'
        self.session = requests.Session()
        
        # Default headers, can be overridden by passing headers during initialization
        self.default_headers = {
            "Authorization": "Token supersecrettoken123",
            "Content-Type": "application/json"
        }

        # Set the session headers
        self.session.headers.update(self.default_headers)

    def list(self):
        return handle_response(self.session.get(self.base_url))

    def retrieve(self, obj_id):
        return handle_response(self.session.get(f"{self.base_url}{obj_id}/"))

    def create(self, data):
        # Use json=data to send the data as JSON in the request
        return handle_response(self.session.post(self.base_url, json=data))

    def update(self, obj_id, data):
        return handle_response(self.session.put(f"{self.base_url}{obj_id}/", json=data))

    def delete(self, obj_id):
        return handle_response(self.session.delete(f"{self.base_url}{obj_id}/"))

    def filter(self, **kwargs):
        """ارسال پارامترهای دلخواه به صورت فیلتر در query string"""
        return handle_response(self.session.get(self.base_url, params=kwargs))