import sqlite3

con = sqlite3.connect("Emails.db")
cur = con.cursor()

# cur.execute(
#     """CREATE TABLE Emails
#                (email text PRIMARY KEY,niche text,website text)"""
# )

# cur.execute(
#     """
#     insert into Emails  values('aaaygjjkmm','hjhhj','knbhj')
# ;

# """
# )

# cur.execute(
#     """
#     insert into Emails  values('bbbygjjsdskmm','hdffjhhj','knbhj')
# ;

# """
# )

# cur.execute(
#     """
#     insert into Emails  values('ccccygjjdfdkmm','hjhhj','knbhj')
# ;

# """
# )

cur.execute(
    """
    SELECT rowid,email,niche,website
FROM Emails;

"""
)

print(cur.fetchall())

con.commit()
con.close()
