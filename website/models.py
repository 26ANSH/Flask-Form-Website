# from . import db as cnxn
# import pyodbc

# def check_user(emailid):
#     cursor = cnxn.cursor()
#     cursor.execute(f"SELECT * FROM UserData WHERE UserEmail='{emailid}'")
#     row_count = cursor.fetchall()
#     if len(row_count) == 0:
#         return False
#     else:
#          cursor.execute(f"INSERT INTO UserData VALUES ('{email}', '{fname}', '{lname}', '{country}');") 
#          cursor.commit()


