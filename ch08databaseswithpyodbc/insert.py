import pyodbc
cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'
names = 'Joe Kate Yates'.split()
ages = '11 13 14'.split()
conn = pyodbc.connect(cs)
cur = conn.cursor() 
for name,age in zip(names,ages):
    sqlStr = f"USE qastore;\nINSERT INTO students VALUES('{name}', {age});"
    result = cur.execute(sqlStr)
    print(result)
conn.commit()
conn.close()
