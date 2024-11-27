import sqlite3
from flask import Flask, request

app = Flask(__name__)

def init_db():
    with sqlite3.connect("sensor.sqlite") as bd:
        bd.execute('''CREATE TABLE IF NOT EXISTS valores (
                        id_medicion INTEGER PRIMARY KEY AUTOINCREMENT,
                        valor_sensor TEXT NOT NULL,
                        time_stamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                      )''')
        bd.commit()

@app.route('/mediciones', methods=['POST'])
def mediciones():
    valorStr = request.form['medicion']
    valor = int(valorStr)

    with sqlite3.connect("sensor.sqlite") as bd:
        bd.execute("INSERT INTO valores (valor_sensor) VALUES (?)", (valor,))
        bd.commit()

    return 'ok'

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
