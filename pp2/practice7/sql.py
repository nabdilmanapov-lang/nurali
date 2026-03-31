#3. Connecting to PostgreSQL
import psycopg2
conn = psycopg2.connect(config)
cur = conn.cursor()

# 4. Creating Tables
cur.execute("""
CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    phone VARCHAR(20)
)
""")
conn.commit()

# 5. Inserting Data
cur.execute(
    "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
    ("Alice", "12345")
)
conn.commit()

# 6. Querying Data (SELECT)
cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()
for row in rows:
    print(row)
  
# 7. Updating Data
cur.execute(
    "UPDATE phonebook SET phone = %s WHERE first_name = %s",
    ("99999", "Alice")
)
conn.commit()

# 8. Deleting Data
cur.execute(
    "DELETE FROM phonebook WHERE first_name = %s",
    ("Alice",)
)
conn.commit()

# 9. Transactions & Error Handling
#Connection manages transactions
#Errors raise exceptions
#Use commit/rollback
try:
    cur.execute("INSERT INTO phonebook VALUES (%s, %s)", ("Test", "123"))
    conn.commit()
except:
    conn.rollback()
