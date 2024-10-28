from ast import Not
import sqlite3 
from sqlite3 import Error
from fastapi import HTTPException, status




class DatabaseConnection:

    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.create_connection()
        return cls._instance


    def create_connection(self):
        try:
            if self._connection is None:
                self._connection = sqlite3.connect("librarypython1.db")
                self._connection.row_factory = sqlite3.Row
        except Error as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


    @staticmethod
    def get_connection():
        return DatabaseConnection()._connection







def create_user_table(db_instance):
    conn = db_instance.get_connection()
    
    if conn is not None:

        try: 
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                verifyOtp BOOLEAN NOT NULL DEFAULT 0,
                createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            conn.commit()

            cursor.execute(""" 
               ALTER TABLE users
               ADD COLUMN otp INTEGER DEFAULT NULL
            """)


            # Create trigger to update 'updatedAt' on row update
            cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS update_user_timestamp
            AFTER UPDATE ON users
            FOR EACH ROW
            BEGIN
                UPDATE users SET updatedAt = CURRENT_TIMESTAMP WHERE id = OLD.id;
            END;
            """)

            conn.commit()


        except Error as e:
            print(e)
        





def create_seller_table(db_instance):
    conn = db_instance.get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                 
            CREATE TABLE IF NOT EXISTS sellers (
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                verifyOtp BOOLEAN NOT NULL DEFAULT 0,
                otp INTEGER DEFAULT NULL,
                createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            cursor.execute("""
               CREATE TRIGGER IF NOT EXISTS update_sellers_timestamp
            AFTER UPDATE ON sellers
            FOR EACH ROW
            BEGIN
                UPDATE users SET updatedAt = CURRENT_TIMESTAMP WHERE id = OLD.id;
            END;
            
            
            """)

            conn.commit()
        
        except Error as e:
            print(str(e))