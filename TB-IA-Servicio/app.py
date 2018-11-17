from flask import Flask, jsonify, request
from Logica_Proposicional import LogicaProposicional as LP

app = Flask(__name__)

Juegos = "Juego1"
Dinero = "Poco"

#esta funcion se activa para solicitudes tanto de GET como de POST
#recibe como parametro un parametro definido en la URL del request
@app.route('/bayesian/<string:name>', methods=['GET', 'POST'])
def hello_world(name):
    
    if request.method == 'POST':
        body = request.get_json()
        edad = body["edad"]
        año = body["año"]
        return jsonify(name=f'Hellow {name}!', data=edad+año, response=True)
    if request.method == 'GET':
    	return jsonify(respuesta= LP(Juegos,Dinero))

#metodo que se encarga de responder cuando la solicitud reqerida no es reconocida por el API
#Summary(la URL que se le solicita al API no esta definida)
@app.errorhandler(404)
def not_found(error):
    return error

if __name__ == "__main__":
    app.run()