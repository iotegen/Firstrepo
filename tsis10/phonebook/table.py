import psycopg2  
con = psycopg2.connect(host = "localhost", database = "Phonebook", user = "postgres", password = "Iliyas2004")
current = con.cursor()
current.execute('''CREATE TABLE PhoneBook(name varchar, number varchar);''')
current.close()
con.commit()
con.close()
