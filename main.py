import json
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorResultadoPartido import ControladorResultadoPartido

controladorCandidato = ControladorCandidato()
controladorMesa = ControladorMesa()
controladorPartido = ControladorPartido()
controladorResultado = ControladorResultado()
controladorResultadoPartido = ControladorResultadoPartido()

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=['GET'])
def test():
    json = {"message": "El servidor se está ejecutando..."}
    return jsonify(json)

@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = controladorCandidato.showallCandidato()
    return jsonify(json)

@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = controladorCandidato.createCandidato(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = controladorCandidato.showidCandidato(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = controladorCandidato.updateCandidato(id, data)
    return jsonify(json)

@app.route("/candidatos/<string:idC>/partido/<string:idP>", methods=['PUT'])
def AsignCandidatoPartido(idC, idP):
    result = controladorCandidato.asigPartido(idC, idP)
    return jsonify(result)

@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = controladorCandidato.deleteCandidato(id)
    return jsonify(json)

@app.route("/mesa", methods=['GET'])
def getMesas():
    json = controladorMesa.showallMesa()
    return jsonify(json)

@app.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = controladorMesa.createMesa(data)
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['GET'])
def getMesa(id):
    json = controladorMesa.showidMesa(id)
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = controladorMesa.updateMesa(id, data)
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = controladorMesa.deleteMesa(id)
    return jsonify(json)

@app.route("/partido", methods=['GET'])
def getPartidos():
    json = controladorPartido.showallPartido()
    return jsonify(json)

@app.route("/partido", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = controladorPartido.createPartido(data)
    return jsonify(json)

@app.route("/partido/<string:id>", methods=['GET'])
def getPartido(id):
    json = controladorPartido.showidPartido(id)
    return jsonify(json)


@app.route("/partido/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = controladorPartido.updatePartido(id, data)
    return jsonify(json)

@app.route("/partido/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = controladorPartido.deletePartido(id)
    return jsonify(json)

@app.route("/resultado", methods=['GET'])
def getResultado():
    json = controladorResultado.showallResultado()
    return jsonify(json)

@app.route("/resultado/<string:id>", methods=['GET'])
def getResultadoid(id):
    json = controladorResultado.showidResultado(id)
    return jsonify(json)

@app.route("/resultado/mesa/<string:idMesa>/candidatos/<string:idCandidatos>", methods=['POST'])
def crearResultadoMesaCandidato(idMesa, idCandidatos):
    data = request.get_json()
    json = controladorResultado.createResultado(data, idMesa, idCandidatos)
    return jsonify(json)


@app.route("/resultado/<string:idR>/mesa/<string:idM>/candidatos/<string:idC>", methods=['PUT'])
def modificarResultados(idR, idM, idC):
    data = request.get_json()
    json = controladorResultado.updateResultado(idR, idM, idC, data)
    return jsonify(json)

@app.route("/resultado/<string:id>", methods=['DELETE'])
def eliminarResultado(id):
    json = controladorResultado.deleteResultado(id)
    return jsonify(json)

@app.route("/resultado/candidato/<string:idC>", methods=['GET'])
def inscritosEnCandidatos(idC):
    json = controladorResultado.listarresultadoscandidato(idC)
    return jsonify(json)


@app.route("/resultadopartido", methods=['GET'])
def getResultadoPartido():
    json = controladorResultadoPartido.showallResultado()
    return jsonify(json)

@app.route("/resultadopartido/<string:id>", methods=['GET'])
def getResultadoPartidoId(id):
    json = controladorResultadoPartido.showidResultado(id)
    return jsonify(json)

@app.route("/resultadopartido/mesa/<string:idMesa>/partido/<string:idPartido>", methods=['POST'])
def crearResultadoMesaPartido(idMesa, idPartido):
    data = request.get_json()
    json = controladorResultadoPartido.createResultado(data, idMesa, idPartido)
    return jsonify(json)


@app.route("/resultadopartido/<string:idR>/mesa/<string:idM>/partido/<string:idP>", methods=['PUT'])
def modificarResultadoPartido(idR, idM, idP):
    data = request.get_json()
    json = controladorResultadoPartido.updateResultado(idR, idM, idP, data)
    return jsonify(json)

@app.route("/resultadopartido/<string:id>", methods=['DELETE'])
def eliminarResultadoPartido(id):
    json = controladorResultadoPartido.deleteResultado(id)
    return jsonify(json)

@app.route("/resultadopartido/partido/<string:id>", methods=['GET'])
def partidosInscritos(id):
    json = controladorResultadoPartido.listarresultadospartido(id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Servidor Corriendo: " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])