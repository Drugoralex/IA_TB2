from flask import Flask, jsonify, request, Response, json
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
       # res = Response(jsonify(respuesta= LP(Juegos,Dinero)), mimetype='application/json')
       data = {
           'respuesta' : LP(Juegos,Dinero)
       }
       js = json.dumps(data)
       res = Response(js, status=200, mimetype='application/json')
       res.headers['Access-Control-Allow-Origin'] = '*'
       res.headers['Access-Control-Allow-Methods'] = "GET"
       res.headers['Access-Control-Allow-Headers'] = "X-Custom-Header"
       return res

#metodo que se encarga de responder cuando la solicitud reqerida no es reconocida por el API
#Summary(la URL que se le solicita al API no esta definida)
@app.errorhandler(404)
def not_found(error):
    return error

if __name__ == "__main__":
    app.run()