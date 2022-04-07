from flask import request, json, Response, Blueprint
from ..models.passenger import passengerModel, passengerSchema


passenger_api = Blueprint('passengers', __name__)
passenger_schema = passengerSchema()

# api endpoint that restrieves all passengers from database
@passenger_api.route('passengers', methods=['GET'])
def get_all():
    passengers = passengerModel.get_all_passengers()
    ser_passengers = passenger_schema.dump(passengers, many=True)

    return custom_response(ser_passengers, 200)

# api endpoint that restrieves a passenger by id from database
@passenger_api.route('passengers/<int:id>', methods=['GET'])
def get_by_id(id):
    passengers = passengerModel.get_passenger(id)
    ser_passengers = passenger_schema.dump(passengers)

    return custom_response(ser_passengers, 200)

# api endpoint that inserts a passenger in the database
@passenger_api.route('passengers', methods=['POST'])
def add_passenger():
    req_data = request.get_json()
    data, error = passenger_schema.load(req_data, partial=True)

    new_passenger = passengerModel(data)
    new_passenger.save()

    ser_data = passenger_schema.dump(new_passenger)

    return custom_response(ser_data, 200)

# wrapper for response
def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )