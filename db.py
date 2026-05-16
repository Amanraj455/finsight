import sqlite3
def connect():
    return sqlite3.connect("database.db")


def create_tables():
    conn = connect()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (email TEXT, date TEXT, category TEXT, amount REAL, type TEXT)''')
    
    
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (email TEXT PRIMARY KEY, password TEXT)''')

    conn.commit()
    conn.close()


def add_transaction(email, date, category, amount, t_type):
    conn = connect()
    c = conn.cursor()

    c.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?)",
              (email, date, category, amount, t_type))

    conn.commit()
    conn.close()

def get_data(email):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT * FROM transactions WHERE email=?", (email,))
    data = c.fetchall()

    conn.close()
    return data


def delete_transaction(email, date, category, amount, t_type):
    conn = connect()
    c = conn.cursor()

    c.execute("""
        DELETE FROM transactions 
        WHERE email=? AND date=? AND category=? AND amount=? AND type=?
    """, (email, date, category, amount, t_type))

    conn.commit()
    conn.close()







   