# # import pyodbc
# from sqlalchemy import create_engine

# conn_str = 'mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 17 for SQL Server};Server=tcp:ansh-db-server.database.windows.net,1433;Database=ansh-db;Uid=ansh-db-server-admin;Pwd=mydbpassword@001;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
# engine_azure = create_engine(conn_str,echo=True)

# print('connection is ok')
# print(engine_azure.table_names())