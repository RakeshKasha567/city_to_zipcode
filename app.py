from flask import Flask, jsonify, request


app = Flask(__name__)

# example data
zip_codes = [
    {
        "city": "NewYork",
        "zip_code": "10001"
    },
    {
        "city": "LosAngeles",
        "zip_code": "90001"
    },
    {
        "city": "Chicago",
        "zip_code": "60601"
    }
]

@app.route('/zipcodes', methods=['GET'])
def get_zipcodes():
    return jsonify(zip_codes)


@app.route('/zipcodes/<string:city_name>/zipcode', methods=['GET'])
def get_zipcode(city_name):
    for zip_code in zip_codes:
        if zip_code['city'] == city_name:
            return zip_code['zip_code']
    return "City not found"


@app.route('/zipcodes', methods=['POST'])
def add_zipcode():
    city = request.json['city']
    zip_code = request.json['zip_code']

    new_zip_code = {
        "city": city,
        "zip_code": zip_code
    }

    zip_codes.append(new_zip_code)
    return jsonify({"message": "Zip code added"})

if __name__ == '__main__':
    
    app.run(host = "0.0.0.0", port =5003)