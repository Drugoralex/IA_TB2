from flask import Flask, jsonify, request, Response, json
from Logica_Proposicional import LogicaProposicional as LP

app = Flask(__name__)

@app.route('/logic', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        body = request.get_json(force=True)
        print(body)
        juegos = body["lista_juegos"]
        dinero = body["dinero"]
        data = {
            'respuesta' : LP(juegos,dinero)
        }
        js = json.dumps(data)
        res = Response(js, status=200, mimetype='application/json')
        res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS"
        res.headers['Access-Control-Allow-Headers'] = "Content-Type"
        return res


@app.errorhandler(404)
def not_found(error):
    return error

if __name__ == "__main__":
    app.run()