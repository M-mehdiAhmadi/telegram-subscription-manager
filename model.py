import sqlite3
import datetime
import os

class BaseModel:
    _DBNAME = os.path.join(os.getcwd(),"database.db")  # esme database o bsh midim
    _primary_key = "id"
    
    @classmethod
    def get_all(cls):
        conn = sqlite3.connect(cls._DBNAME) #etesal be database
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {cls.__name__}")
        rows = cur.fetchall()
        conn.close()
        return [cls(**dict(zip([column[0] for column in cur.description], row))) for row in rows]
    
    import sqlite3
import os

class BaseModel:
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

        













class User(BaseModel):
    _primary_key = "chat_id"
    def __init__(self,chat_id,time_created,is_active,phone,is_admin,language):
        self.chat_id = chat_id
        self.time_created = time_created
        self.is_active = is_active
        self.phone = phone
        self.is_admin = is_admin
        self.language = language
    @classmethod
    def get_by_chat_id(cls,chat_id):
        conn = sqlite3.connect(cls._DBNAME) 
        cur = conn.cursor() 
        
        cur.execute(f"SELECT * FROM {cls.__name__} WHERE chat_id={chat_id}")
        row = cur.fetchone()
        conn.close()
        return cls(*row) if row else None
    
        
class Channel (BaseModel):
    def __init__(self,id,name,chat_id):
        self.id = id
        self.name = name
        self.chat_id = chat_id
        
class Subtraction (BaseModel):
    def __init__(self,id,price,name,channel):
        self.id = id
        self.price = price
        self.channel = channel
        self.name = name
class Joinforce (BaseModel):
    def __init__(self,id,link,name):
        self.id = id
        self.link = link
        self.name = name
class Payment (BaseModel):
    def __init__(self,id,user,subtraction,invoice_id,invoice_link,date):
        self.id = id
        self.user = user
        self.subtraction = subtraction
        self.invoice_id = invoice_id
        self.invoice_link = invoice_link
        self.date = date
class User2subscription (BaseModel):
    def __init__(self,user,sub,date,id,link,chat_id):
        self.user = user
        self.sub = sub
        self.date = date
        self.id = id
        self.link = link
        self.chat_id = chat_id


