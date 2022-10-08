from Callboard import app
from creat_db import Connect_db

if __name__ == '__main__':
    connect_db = Connect_db()
    if connect_db.check_existing_db():
        connect_db.create_database()
    app.run(debug=True)
