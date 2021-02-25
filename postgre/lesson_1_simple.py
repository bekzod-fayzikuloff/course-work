import psycopg2

conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='narutokun',
    host='localhost',
)

cursor = conn.cursor()
cursor.execute('SELECT FROM employee LIMIT 10')
records = cursor.fetcall()

for i in records:
    print(records)

cursor.close()
conn.close()
