import sqlite3

## connect to your db file
conn = sqlite3.connect('first.db')

## execute queries against a databse
cur = conn.cursor()

## the SQL query
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   username TEXT,
   money_entry INT,
   piggy_bank_amount INT,
   debt_amount INT);
""")

conn.commit()