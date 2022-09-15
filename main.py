from Callboard import app
from creat_db import create_database

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
