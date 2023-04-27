
import psycopg2, csv

# Connect to the database
conn = psycopg2.connect(
    host='localhost',
    dbname='Phonebook',
    user='postgres',
    password='Iliyas2004',
)
cur = conn.cursor()
def disentry(page):
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    i = 0
    limit = 10 * page
    for row in rows:
        if i < limit and i >= limit - 10:
            print(row)
        i+=1
    print(f"Page 1 / {len(rows) // 10 + 1}")
    page = input("Enter page or Q for quit: ")
    if page == "Q" or page == "q":
        page = 1000
    if 1 <= int(page) <= len(rows) // 10 + 1:
        disentry(page)
    conn.commit()
def datausers(data):
    incorrect = []
    for d in data:
        name, number = d
        if len(number) != 4 or not number.isdigit():
            incorrect.append(d)
            continue
        cur.execute("INSERT INTO PhoneBook (name, number) VALUES (%s, %s)", (name, number))
    print(incorrect)
    conn.commit()
    cur.close()
    
def update(name, number):
    cur.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name,))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute("INSERT INTO phonebook (name, number) VALUES (%s, %s)", (name, number,))
    else:
        cur.execute("UPDATE phonebook SET number = %s WHERE name = %s", (number, name,))
    conn.commit()
    cur.close()
while True:
    print("1 - insert csv, 2 - insert console, 3 - update, 4 - search, 5 - search part, 6 - select, 7 - delete, 8 - exit, 9 - datausers")
    n = input()
    if n == '1':
        file = input("File name:")
        with open(file+".csv", "r") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    cur.execute("""INSERT INTO PhoneBook VALUES(%s,%s) returning *;""", row)
                conn.commit()
    elif n == '2':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        cur.execute("INSERT INTO phonebook (name, number) VALUES (%s, %s)", (name, number))
        conn.commit()
    elif n == '3':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        update(name, number)
    elif n == '4':
        name = input("Enter name to search: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (name,))
        rows = cur.fetchall()
        for r in rows:
            print(r)
        conn.commit()
    elif n == '5':
        part = input("Enter part to search: ")
        cur.execute(f"SELECT * FROM phonebook WHERE name ILIKE %s OR number ILIKE %s", ('%'+part+'%', '%'+part+'%'))
        rows = cur.fetchall()
        cur.close()
        for row in rows:
            print(row)
        conn.commit()
    elif n == '6':
        disentry(1)
    elif n == '7':  
        part = input("delete name of part or phone:")
        cur.execute("DELETE FROM phonebook WHERE name ILIKE %s OR number ILIKE %s", ('%'+part+'%', '%'+part+'%',))
        conn.commit()
    elif n == '8':
        break
    elif n == '9':
        data = [("Ippoe", "1234"), ("Uzaki", "9877"), ("Tyson", "11564")]
        datausers(data)
    else:
        print("Please try again, your server is loser")
     

conn.close()