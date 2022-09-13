import psycopg2
import config_db


class Connector:
    def __init__(self):
        self.conn = psycopg2.connect(database=config_db.DATABASE, user=config_db.USER, password=config_db.PASSWORD)
        self.conn.autocommit = True
        self.cursor_db = self.conn.cursor()

    def add_user(self, user_id):
        sql_add_user = f"INSERT INTO users (user_id)" \
                         f"VALUES ('{user_id}')" \
                         f"ON CONFLICT (user_id) DO NOTHING"
        self.cursor_db.execute(sql_add_user)

    def add_ad(self, ads_id, title, text_ad, user_id):
        sql_add_ad = f"INSERT INTO ads (ads_id, title, text_ad, user_id)" \
                        f"VALUES ('{ads_id}', '{title}', '{text_ad}', {user_id})" \
                        f"ON CONFLICT (ads_id) DO NOTHING"
        self.cursor_db.execute(sql_add_ad)

    def del_ad(self, ads_id):
        sql_del_ad = f"DELETE FROM ads WHERE ads_id = {ads_id}"
        self.cursor_db.execute(sql_del_ad)

    def show_ad(self, user_id):
        sql_show_ad = f"SELECT title, text_ad FROM pair WHERE user_id = {user_id}"
        self.cursor_db.execute(sql_show_ad)
        ad = self.cursor_db.fetchone()
        return ad
