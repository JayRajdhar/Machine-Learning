import mysql.connector as conn

db = conn.connect(host = "localhost",
                  user = "root",
                  passwd = "statiq1234",
                  database = "statiq_db")
cur = db.cursor()
insert_query = "create table newusers(name varchar(255) primary key, password varchar(255 ))"
cur.execute(insert_query)
db.commit()
db.close()