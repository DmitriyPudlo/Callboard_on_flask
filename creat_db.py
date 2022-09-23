import psycopg2
import config_db


def create_db(cursor):
    sql_create_database = f'CREATE DATABASE {config_db.DATABASE}'
    cursor.execute(sql_create_database)


def check_existing_db(cursor):
    sql_db_exists = f"SELECT datname FROM pg_catalog.pg_database WHERE datname = '{config_db.DATABASE}'"
    cursor.execute(sql_db_exists)
    if not cursor.fetchall():
        create_db(cursor)


def create_tables(cursor):
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
    cursor.execute(sql_create_table)


def create_database():
    conn_checking_db = psycopg2.connect(user=config_db.USER, password=config_db.PASSWORD)
    conn_checking_db.autocommit = True
    cursor_db = conn_checking_db.cursor()
    check_existing_db(cursor_db)
    create_tables(cursor_db)
    conn_checking_db.close()
