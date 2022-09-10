from flask import Flask, request, jsonify
import csv

server = Flask(__name__)

@server.route('/form', methods=['POST'])
def input_data():
    number_of_passengers = int(request.json["number_of_passengers"])
    home_planet = request.json["HomePlanet"]
    cryo_sleep = request.json["CryoSleep"]
    cabin = request.json["Cabin"]
    destination = request.json["Destination"]
    age = request.json["Age"]
    vip = request.json["VIP"]
    room_service = request.json["RoomService"]
    food_court = request.json["FoodCourt"]
    shopping = request.json["Shopping"]
    spa = request.json["Spa"]
    vrdeck = request.json["VRDeck"]
    name = request.json["Name"]

    df_header = ['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'Age', 'VIP', 'RoomService', 'FoodCourt', 'Shopping', 'Spa', 'VRDeck', 'Name']
    with open('test.csv', 'w', encoding='UTF8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(df_header)
                for i in range(0, number_of_passengers):
                    input_data = [home_planet[i], cryo_sleep[i], cabin[i], destination[i], age[i], vip[i], room_service[i], food_court[i], shopping[i], spa[i], vrdeck[i], name[i]]
                    df_data = input_data
                    writer.writerow(df_data)
    return jsonify({"message": "Success"}), 200


@server.route('/test', methods=['POST'])
def test_post():
    test = request.json["name"]
    print(test)
    return jsonify({"message": "Success", "name": test}), 200


if __name__ == '__main__':
    server.run(debug=True,host='0.0.0.0',port='8080')
