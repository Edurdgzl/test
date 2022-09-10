from flask import Flask, request, jsonify, render_template
import numpy as np

#Cargar el modelo
#dt = load('modelo.joblib')

#Generar el servidor (Back-end)
server = Flask(__name__)


""" @server.route("/formulario",methods=['GET'])
def formulario():
    return render_template('pagina.html') """

#Envio de datos a través de Archivos
""" @servidorWeb.route('/modeloFile', methods=['POST'])
def modeloFile():
    f = request.files['file']
    filename=secure_filename(f.filename)
    path=os.path.join(os.getcwd(),'files',filename)
    f.save(path)
    file = open(path, "r")
    
    for x in file:
        info=x.split()
    print(info)
    datosEntrada = np.array([
            float(info[0]),
            float(info[1]),
            float(info[2])
        ])
    #Utilizar el modelo
    resultado=dt.predict(datosEntrada.reshape(1,-1))
    #Regresar la salida del modelo
    return jsonify({"Resultado":str(resultado[0])}) """

@server.route('/form', methods=['POST'])
def input_data():
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
    input_data = np.array([home_planet, cryo_sleep, cabin, destination, age, vip, room_service, food_court, shopping, spa, vrdeck, name])
    return jsonify({"message": "Success"}), 200


@server.route('/test', methods=['POST'])
def test_post():
    test = request.json["name"]
    print(test)
    return jsonify({"message": "Success", "name": test}), 200


if __name__ == '__main__':
    server.run(debug=True,host='0.0.0.0',port='8080')
