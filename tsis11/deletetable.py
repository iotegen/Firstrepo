import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host='localhost',
    dbname='Phonebook',
    user='postgres',
    password='Iliyas2004',
)

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create the phonebook table
cur.execute("CREATE TABLE phonebook2 (name VARCHAR(50), number VARCHAR(20))")

# Commit the changes
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()