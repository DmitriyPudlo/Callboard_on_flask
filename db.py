import psycopg2
import config_db


class Connector:
    def __init__(self):
        self.conn = psycopg2.connect(database=config_db.DATABASE, user=config_db.USER, password=config_db.PASSWORD)
        self.conn.autocommit = True
        self.cursor_db = self.conn.cursor()

    def add_user(self, login, email, password):
        sql_add_user = f"INSERT INTO users (login, email, password)" \
                       f"VALUES ('{login}', '{email}', '{password}')"
        self.cursor_db.execute(sql_add_user)

    def add_ad(self, title, text_ad, time, user_id):
        sql_add_ad = f"INSERT INTO ads (title, text_ad, time, user_id)" \
                     f"VALUES ('{title}', '{text_ad}', '{time}', {user_id})"
        self.cursor_db.execute(sql_add_ad)

    def del_ad(self, ad_id):
        sql_del_ad = f"DELETE FROM ads WHERE ad_id = '{ad_id}'"
        self.cursor_db.execute(sql_del_ad)

    def show_ad_on_ad(self, ad_id):
        sql_show_ad = f"SELECT * FROM ads WHERE ad_id = '{ad_id}'"
        self.cursor_db.execute(sql_show_ad)
        ad = self.cursor_db.fetchone()
        response = [{'ad_id': ad[0],
                     'title': ad[1],
                     'text_ad': ad[2],
                     'time:': ad[3],
                     'user_id': ad[4]}]
        return response

    def show_user_id_on_ad(self, ad_id):
        sql_show_ad = f"SELECT user_id FROM ads WHERE ad_id = '{ad_id}'"
        self.cursor_db.execute(sql_show_ad)
        ad = self.cursor_db.fetchone()
        return ad[0]

    def show_ad_on_user(self, user_id):
        sql_show_ad = f"SELECT title, text_ad, time FROM ads WHERE user_id = '{user_id}'"
        self.cursor_db.execute(sql_show_ad)
        ad = self.cursor_db.fetchone()
        return ad

    def show_user(self, user_id):
        sql_show_user = f"SELECT * FROM users WHERE user_id = '{user_id}'"
        self.cursor_db.execute(sql_show_user)
        user = self.cursor_db.fetchone()
        return user

    def show_all(self):
        sql_show_ad = f"SELECT * FROM ads"
        self.cursor_db.execute(sql_show_ad)
        ads = self.cursor_db.fetchall()
        response = []
        for ad in ads:
            response.append({'ad_id': ad[0],
                             'title': ad[1],
                             'text_ad': ad[2],
                             'time:': ad[3],
                             'user_id': ad[4]})
        return response

    def check_authenticated(self, login, password):
        sql_check = f"SELECT user_id FROM users WHERE login = '{login}' and password = '{password}'"
        self.cursor_db.execute(sql_check)
        user_id = self.cursor_db.fetchone()
        return user_id[0]

    def check_email(self, email):
        sql_check = f"SELECT email FROM users WHERE email = '{email}'"
        self.cursor_db.execute(sql_check)
        email = self.cursor_db.fetchone()
        return email[0]

    def update(self, ad_id, title=None, text_ad=None):
        if title:
            sql_update_title = f"UPDATE ads SET title = '{title}' WHERE ad_id = '{ad_id}'"
            self.cursor_db.execute(sql_update_title)
        if text_ad:
            sql_update_text = f"UPDATE ads SET text_ad = '{text_ad}' FROM ads WHERE ad_id = '{ad_id}'"
            self.cursor_db.execute(sql_update_text)
