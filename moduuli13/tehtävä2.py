from flask import Flask, jsonify
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="lentopeli",
    user="nuni",
    password="nuni",
    autocommit=True,
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

if connection.is_connected():
    print("Connected to the database")
else:
    print("Connection failed")

cursor = connection.cursor()

app = Flask(__name__)

@app.route("/kenttä/<icao>")
def kentta(icao):
    sql = 'SELECT ident, NAME, municipality FROM airport WHERE ident = %s'
    print("SQL Query:", sql)  # Debug print
    cursor.execute(sql, (icao,))
    results = cursor.fetchall()
    print("Results:", results)  # Debug print
    if results:
        return jsonify({"ICAO": results[0][0], "Name": results[0][1], "Municipality": results[0][2]})
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4999)