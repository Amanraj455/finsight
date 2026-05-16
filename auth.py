import sqlite3

class AuthManager:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()

    def register_user(self, email, password):
        try:
            self.c.execute("INSERT INTO users VALUES (?, ?)", (email, password))
            self.conn.commit()
            return True
        except:
            return False

    def login_user(self, email, password):
        self.c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        return self.c.fetchone() is not None