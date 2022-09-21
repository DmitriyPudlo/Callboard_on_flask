import psycopg2
import config_db


class Connector:
    def __init__(self):
        self.conn = psycopg2.connect(database=config_db.DATABASE, user=config_db.USER, password=config_db.PASSWORD)
        self.conn.autocommit = True
        self.cursor_db = self.conn.cursor()

    def add_user(self, login, email, password):
        sql_add_user = f"INSERT INTO users (login, email, password)" \
                         f"VALUES ('{login}', '{email}', '{password}')" \
                         f"ON CONFLICT (user_id) DO NOTHING"
        self.cursor_db.execute(sql_add_user)

    def add_ad(self, title, text_ad, time, user_id):
        sql_add_ad = f"INSERT INTO ads (title, text_ad, time, user_id)" \
                        f"VALUES ('{title}', '{text_ad}', '{time}', {user_id})" \
                        f"ON CONFLICT (user_id) DO NOTHING"
        self.cursor_db.execute(sql_add_ad)

    def del_ad(self, ads_id):
        sql_del_ad = f"DELETE FROM ads WHERE ads_id = {ads_id}"
        self.cursor_db.execute(sql_del_ad)

    def show_ad_on_ad(self, ad_id):
        sql_show_ad = f"SELECT title, text_ad, time, user_id FROM ads WHERE ad_id = {ad_id}"
        self.cursor_db.execute(sql_show_ad)
        ad = self.cursor_db.fetchone()
        return ad

    def show_ad_on_user(self, user_id):
        sql_show_ad = f"SELECT title, text_ad, time FROM ads WHERE user_id = {user_id}"
        self.cursor_db.execute(sql_show_ad)
        ad = self.cursor_db.fetchone()
        return ad

    def show_user(self, user_id):
        sql_show_user = f"SELECT * FROM user WHERE user_id = {user_id}"
        self.cursor_db.execute(sql_show_user)
        user = self.cursor_db.fetchone()
        return user

    def show_all(self):
        sql_show_ad = f"SELECT * FROM ads"
        self.cursor_db.execute(sql_show_ad)
        ad = self.cursor_db.fetchone()
        return ad

    def check_authenticated(self, login, password):
        sql_check = f"SELECT user_id FROM user WHERE login = {login} and password = {password}"
        self.cursor_db.execute(sql_check)
        user_id = self.cursor_db.fetchone()
        return user_id

