''' file connects to the postgresql database'''
import psycopg2
import uuid

class MyDatabase():
    def __init__(self):
        try:
            self.db = 'sample_db'
            connection = '''dbname={} user=lubwama password=lubwama1'''
            self.conn = psycopg2.connect(connection.format(self.db))
            self.cur = self.conn.cursor()
            self.conn.autocommit =True
            print(self.db)
        except Exception as e:
            print(e)
            print("Database connection failed")