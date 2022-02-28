
from flask import Flask
from flask import request, make_response, jsonify
from main import create_tables
from flask_cors import CORS
import json
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

@app.route("/sitsiplasutin", methods=["POST", "GET"])
def create_seating():
    # TODO Add data validation, Better Data parses, Error handling, Schema
    try:
        form_data = json.loads(request.form["json"])
        poydat = list((form_data["table_sizes"]).split(","))
        poydat = list(map(int, poydat))

        sitsers_csv = request.files["sitsers_csv"]

        filled_tables = create_tables(poydat=poydat, sitsers=sitsers_csv)

        json_data = []
        for i in range(0, len(filled_tables)):
            json_data.append((filled_tables[i].tolist()))
        
        response = make_response(jsonify(json_data), 200)
        
        return response
    
    except Exception as err:
        logging.warning('Nyt meni jottain vikkaan')
        logging.warning(err)
        return make_response("SÄRKI", 400)

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')

