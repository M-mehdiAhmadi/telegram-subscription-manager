import csv
import os
import datetime
from model import (
    BaseModel, User, Channel, Subscriptions,
    Payment, User2subscriptions, Joinforce, Specialuser
)


class ExportClient:

    MODEL_MAP = {
        "users": User,
        "channel": Channel,
        "subscriptions": Subscriptions,
        "payment": Payment,
        "user2subscriptions": User2subscriptions,
        "joinforce": Joinforce,
        "specialuser": Specialuser,
    }

    def fetch_data(self, table_name: str):
        model = self.MODEL_MAP.get(table_name.lower())
        if not model:
            raise ValueError(f"No model defined for table: {table_name}")
        return model.get_all()

    def save_csv(self, objects: list, file_path: str):
        if not objects:
            raise ValueError("No data to export!")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Get field names from the first object's __dict__
        fieldnames = [k for k in objects[0].__dict__.keys() if not k.startswith('_')]

        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for obj in objects:
                writer.writerow({k: getattr(obj, k) for k in fieldnames})

        return file_path

    def export(self, table_name: str, output_dir: str = "exports") -> str:
        data = self.fetch_data(table_name)
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = os.path.join(output_dir, f"{table_name}_{timestamp}.csv")
        return self.save_csv(data, file_path)
