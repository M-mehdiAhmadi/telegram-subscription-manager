import requests
import csv
import os
from api_client.base import BaseAPIClient

class ExportClient:
    
    def __init__(self):
        self.endpoints = {
            "channels": "vi/api/channels/",
            "subscriptions": "vi/api/subscriptions/",
            "user2subscriptions": "vi/api/user2subscriptions/",
            "specialusers": "vi/api/specialusers/",
            "payments": "vi/api/payments/",
            "joinforce": "vi/api/joinforce/",
            "users": "core/user/users/",  # فرض بر اینه که endpoint کاربران اینه
        }
        self.api = BaseAPIClient(base_url="")  # چون آدرس‌ها کامل نیستن، اینجا خالی می‌ذاریم

    def fetch_data(self, table_name):
        endpoint = self.endpoints.get(table_name.lower())
        if not endpoint:
            raise ValueError(f"❌ No endpoint defined for table: {table_name}")
        url = self.api.base_url + endpoint
        response = self.api.session.get(url)
        response.raise_for_status()
        return response.json()

    def save_csv(self, data, file_path):
        if not data:
            raise ValueError("❌ No data received!")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        return file_path
