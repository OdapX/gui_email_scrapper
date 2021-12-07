import sqlite3

con = sqlite3.connect('Emails.db')
cur = con.cursor()

# cur.execute('''CREATE TABLE Emails
#                (email text PRIMARY KEY,niche text,website text)''')


cur.execute("""
    SELECT *
FROM Emails;

""")

print(cur.fetchall())

con.commit()
con.close()
