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

    # Make a request to the weather microservice
    weather_url = f"http://172.17.0.2:5004/{zip_code}" 
    weather_response = request.get(weather_url)
    
    # Check the response status code
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        new_zip_code = {
            "city": city,
            "zip_code": zip_code,
            "weather": weather_data
        }
    else:
        return "Error retrieving weather data", weather_response.status_code

    zip_codes.append(new_zip_code)
    return jsonify({"message": "Zip code and weather data added"})


if __name__ == '__main__':
    
    app.run(host = "0.0.0.0", port =5003)
