import mysql.connector as conn
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/register/<string:name>/<string:password>')
def insert(name, password):
    db = conn.connect(host="localhost",
                      user="root",
                      passwd="statiq1234",
                      database="statiq_db")
    cur = db.cursor()

    insert_query= "INSERT INTO newusers VALUES('{}', '{}')".format(name, password)
    cur.execute(insert_query)
    db.commit()
    db.close()
    return jsonify({'message': 'user addded'})

app.run(port = 5000)