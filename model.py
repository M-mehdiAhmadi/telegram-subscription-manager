import sqlite3
import datetime
import os
import csv


class BaseModel:
    """
    Base class for all models in the application.
    This class provides methods for saving, deleting, and filtering records in the database.
    """
    _DBNAME = os.path.join(os.getcwd(), "database.db") 
    _primary_key = "id"  # همه کلاس‌ها میتونن override کنن اگر لازم بود

    def save(self):
        table_name = self.__class__.__name__
        pk = self._primary_key

        fields = [k for k in self.__dict__.keys() if not k.startswith('_') and not callable(getattr(self, k))]
        values = [getattr(self, field) for field in fields]
        id_val = getattr(self, pk, None) if pk in fields else None

        conn = sqlite3.connect(self._DBNAME)
        cur = conn.cursor()

        if id_val is None:
            # INSERT
            columns = ", ".join(fields)
            placeholders = ", ".join(["?"] * len(fields))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cur.execute(query, values)
            if pk == "id":  # فقط اگر کلید اولیه id بود
                setattr(self, "id", cur.lastrowid)
        else:
            # UPDATE
            assignments = ", ".join([f"{key}=?" for key in fields])
            values.append(id_val)
            query = f"UPDATE {table_name} SET {assignments} WHERE {pk}=?"
            cur.execute(query, values)

        conn.commit()
        conn.close()

    def delete(self):
        """
        Deletes the current instance from the database.
        """
        table_name = self.__class__.__name__
        pk = self._primary_key

        conn = sqlite3.connect(self._DBNAME)
        cur = conn.cursor()

        query = f"DELETE FROM {table_name} WHERE {pk} = ?"
        cur.execute(query, (getattr(self, pk),))

        conn.commit()
        conn.close()
    @classmethod
    def filter(cls, **kwargs):
        conn = sqlite3.connect(cls._DBNAME)
        cur = conn.cursor()

        if not kwargs:
        # اگر شرطی نفرستاده بودن، همه رکوردها رو بده
            cur.execute(f"SELECT * FROM {cls.__name__}")
        else:
            conditions = " AND ".join([f"{key}=?" for key in kwargs])
            values = list(kwargs.values())
            query = f"SELECT * FROM {cls.__name__} WHERE {conditions}"
            cur.execute(query, values)

        rows = cur.fetchall()
        columns = [column[0] for column in cur.description]
        conn.close()
        return [cls(**dict(zip(columns, row))) for row in rows]
    @classmethod
    def get_all(cls, limit=None, offset=None):
        """
        Returns all records from the table corresponding to the model class,
        with optional pagination (limit, offset).
        
        :param limit: Number of records to fetch (Optional)
        :param offset: Number of records to skip before starting to fetch (Optional)
        :return: List of model instances
        """
        conn = sqlite3.connect(cls._DBNAME)
        cur = conn.cursor()

        query = f"SELECT * FROM {cls.__name__}"
        
        # Adding pagination (limit and offset)
        if limit is not None:
            query += f" LIMIT ?"
        if offset is not None:
            query += f" OFFSET ?"

        values = []
        if limit is not None:
            values.append(limit)
        if offset is not None:
            values.append(offset)

        try:
            cur.execute(query, values)
            rows = cur.fetchall()
            columns = [column[0] for column in cur.description]
            conn.close()

            # Mapping rows to the model instances
            return [cls(**dict(zip(columns, row))) for row in rows]
        except sqlite3.Error as e:
            conn.close()
            print(f"An error occurred: {e}")
            return []

    @classmethod
    def get_model_by_table_name(cls, table_name: str):
        for subclass in cls.__subclasses__():
            if subclass.__name__.lower() == table_name.lower():
                return subclass
        return None
    
    @classmethod
    def export_to_csv(cls, output_dir="exports"):
        table_name = cls.__name__
        db_path = cls._DBNAME

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # بررسی وجود جدول
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if not cur.fetchone():
            conn.close()
            raise ValueError(f"❌ Table '{table_name}' does not exist in database.")

        # گرفتن داده‌ها
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        conn.close()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        filename = f"{table_name.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(rows)

        return filepath  # مسیر فایل CSV
    
    
class User(BaseModel):
    _primary_key = "chat_id"
    def __init__(self, chat_id, time_created, is_active, phone, is_admin, language, is_special=0):
        self.chat_id = chat_id
        self.time_created = time_created
        self.is_active = is_active
        self.phone = phone
        self.is_admin = is_admin
        self.language = language
        self.is_special = is_special

    @classmethod
    def get_by_chat_id(cls, chat_id):
        conn = sqlite3.connect(cls._DBNAME)
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM {cls.__name__} WHERE chat_id=?", (chat_id,))
        row = cur.fetchone()
        conn.close()
        return cls(*row) if row else None
    
        
class Channel (BaseModel):
    def __init__(self, id, name, chat_id, link=None):
        self.id = id
        self.name = name
        self.chat_id = chat_id
        self.link = link
        
class Subscriptions (BaseModel):
    def __init__(self, id, price, name, channel, day):
        self.id = id
        self.price = price
        self.name = name
        self.channel = channel
        self.day = day

class Joinforce (BaseModel):
    def __init__(self,id,link,name):
        self.id = id
        self.link = link
        self.name = name
class Payment (BaseModel):
    def __init__(self,id,user,subscriptions,invoice_id,invoice_link,date):
        self.id = id
        self.user = user
        self.subscriptions = subscriptions
        self.invoice_id = invoice_id
        self.invoice_link = invoice_link
        self.date = date
class User2subscriptions (BaseModel):
    def __init__(self,user,subscriptions,date,id,link,chat_id):
        self.user = user
        self.subscriptions = subscriptions
        self.date = date
        self.id = id
        self.link = link
        self.chat_id = chat_id

class Specialuser(BaseModel):
    def __init__(self, id, user, channel):
        self.id = id  # Primary key
        self.user = user  # References User (chat_id)
        self.channel = channel  # References Channel (id)


