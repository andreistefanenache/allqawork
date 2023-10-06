import pyodbc
cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'
sqlStr = "USE qastore;CREATE TABLE dbo.students (name VARCHAR(30) PRIMARY KEY, age INTEGER);"
conn = pyodbc.connect(cs)
cur = conn.cursor() 
result = cur.execute(sqlStr)
conn.close()
print(result)
