import pyodbc
cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

conn = pyodbc.connect(cs)
cur = conn.cursor()
result = cur.execute('SELECT * FROM company;').fetchall()
conn.close()
print(result)
