
from flask import Flask
from flask import send_file, Response, send_from_directory, request

from main import create_tables
import io
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.route("/sitsiplasutin", methods=['POST'])
def create_seating():

    json = request.json
    print(request)
    print(json)
    poydat = [30, 10]
    csv_file = create_tables(poydat=poydat, sitsers="./datafiles/sample.xlsx")

    mem = io.BytesIO()
    mem.write(csv_file.getvalue().encode())
    
    # seeking was necessary. Python 3.5.2, Flask 0.12.2
    mem.seek(0)
    csv_file.close()

    return send_file(
        mem,
        as_attachment=True,
        attachment_filename='plaseeraus.csv',
        mimetype='text/csv'
    )


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')

