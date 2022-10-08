import psycopg2
import config_db


class Connect_db:
    def __init__(self):
        self.conn_checking_db = psycopg2.connect(user=config_db.USER, password=config_db.PASSWORD)
        self.conn_checking_db.autocommit = True
        self.cursor_db = self.conn_checking_db.cursor()

    def create_db(self):
        sql_create_database = f'CREATE DATABASE {config_db.DATABASE}'
        self.cursor_db.execute(sql_create_database)

    def check_existing_db(self):
        sql_db_exists = f"SELECT datname FROM pg_catalog.pg_database WHERE datname = '{config_db.DATABASE}'"
        self.cursor_db.execute(sql_db_exists)
        if self.cursor_db.fetchall():
            return

    def create_tables(self):
        sql_create_table = 'CREATE TABLE IF NOT EXISTS users (' \
                           'user_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,' \
                           'login VARCHAR(20) NOT NULL,' \
                           'email VARCHAR(20) unique,' \
                           'password VARCHAR(20) NOT NULL,' \
                           'CONSTRAINT users_pkey PRIMARY KEY (user_id));' \
                           'CREATE TABLE IF NOT EXISTS ads (' \
                           'ad_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,' \
                           'title VARCHAR(20) NOT NULL,' \
                           'text_ad VARCHAR(500) NOT NULL,' \
                           'time VARCHAR(12) NOT NULL,' \
                           'user_id INT,' \
                           'CONSTRAINT ads_pkey PRIMARY KEY (ad_id),' \
                           'FOREIGN KEY (user_id) REFERENCES users (user_id));'
        self.cursor_db.execute(sql_create_table)

    def create_database(self):
        self.create_db()
        self.create_tables()
        self.conn_checking_db.close()
