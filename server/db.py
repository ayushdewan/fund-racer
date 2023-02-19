import sqlite3

conn = sqlite3.connect('test.db', check_same_thread=False)
cur = conn.cursor()

cur.execute("CREATE TABLE streams (id INTEGER, name TEXT, label TEXT, description TEXT, recipient TEXT, goal INTEGER, raised INTEGER, token TEXT)")

def insert_row(id, name, label, description, recipient, goal, token):
    cur.execute(f"INSERT INTO streams VALUES ({id}, '{name}', '{label}', '{description}', '{recipient}', {goal}, 0, '{token}')")

insert_row(4785876, "s", "abcdef", "a demo stream", "American Red Cross", 5000, "28f033e2b1c8d05d53b9c7b2fb9ae0568f34292be94132fa0c7afbcceb3746ab")

