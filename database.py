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
# )\

cur.execute(
    """
                SELECT min(rowid)
                FROM Emails ;

                        """
)
print(cur.fetchall()[0])
cur.execute(
    """
                SELECT max(rowid)
                FROM Emails ;

                        """
)

print(cur.fetchall()[0])

con.commit()
con.close()
