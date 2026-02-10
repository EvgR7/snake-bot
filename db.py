import sqlite3


def init_db():
    conn = sqlite3.connect('score.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS scores (user_id INTEGER PRIMARY KEY, max_score INTEGER NOT NULL)""")
    conn.commit()
    conn.close()


def get_max_score(user_id: int):
    conn = sqlite3.connect('score.db')
    cursor = conn.cursor()
    cursor.execute("SELECT max_score FROM scores WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 0


def update_max_score(user_id, score):
    conn = sqlite3.connect('score.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO scores (user_id, max_score)
                    VALUES(?,?) ON CONFLICT(user_id)
                    DO UPDATE SET max_score = excluded.max_score""",(user_id,score))
    conn.commit()
    conn.close()