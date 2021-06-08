# mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 17 for SQL Server};Server=tcp:ansh-db-server.database.windows.net,1433;Database=ansh-db;Uid=ansh-db-server-admin;Pwd=mydbpassword@001;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
import pyodbc
import textwrap

#  Connection Parameters
driver = "{ODBC Driver 17 for SQL Server}"
server_name = "ansh-db-server"
database_name = "ansh-db"
server =  f'{server_name}.database.windows.net,1433'
username = 'ansh-db-server-admin'
password = 'mydbpassword@001'

# Connection String
conn_url = f"Driver={driver};Server=tcp:{server};Database={database_name};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

#Connection STARTED
cnxn = pyodbc.connect(conn_url)
print("Connection OPEN")


# Run Querry


cursor = cnxn.cursor()
cursor.execute("INSERT INTO UserData VALUES (0003, '19bcs4085@cuchd.in', 'Lakshay', 'Chhabra');") 
cursor.commit()
# cursor.update("INSERT INTO UserData VALUES (0003, '19bcs4085@cuchd.in', 'Lakshay', 'Chhabra');") 
# cursor.execute("SELECT * FROM UserData") 
# row = cursor.fetchone() 
# while row:
#     print(row)
#     row = cursor.fetchone()





# Connection CLOSED
cnxn.close()
print("Connection CLOSE")