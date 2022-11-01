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

controladorCandidato = ControladorCandidato()
controladorMesa = ControladorMesa()
controladorPartido = ControladorPartido()
controladorResultado = ControladorResultado()

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods = ['GET'])
def test():
    json = {"message": "El servidor se está ejecutando..."}
    return jsonify(json)

@app.route("/Candidatos", methods = ['GET'])
def getCandidatos():
    json = controladorCandidato.showallCandidato()
    return jsonify(json)

@app.route("/Candidatos", methods = ['POST'])
def crearCandidato():
    data = request.get_json()
    json = controladorCandidato.createCandidato(data)
    return jsonify(json)

@app.route("/Candidatos/<string:id>", methods = ['GET'])
def getCandidato(id):
    json = controladorCandidato.showidCandidato(id)
    return jsonify(json)

@app.route("/Candidatos/<string:id>", methods = ['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = controladorCandidato.updateCandidato(id, data)
    return jsonify(json)

@app.route("/Candidatos/<string:idC>/Partido/<string:idP>", methods = ['PUT'])
def AsignCandidatoPartido(idC, idP):
    result = controladorCandidato.asigPartido(idC, idP)
    return jsonify(result)

@app.route("/Candidatos/<string:id>", methods = ['DELETE'])
def eliminarCandidato(id):
    json = controladorCandidato.deleteCandidato(id)
    return jsonify(json)

@app.route("/Mesa", methods = ['GET'])
def getMesas():
    json = controladorMesa.showallMesa()
    return jsonify(json)

@app.route("/Mesa", methods = ['POST'])
def crearMesa():
    data = request.get_json()
    json = controladorMesa.createMesa(data)
    return jsonify(json)

@app.route("/Mesa/<string:id>", methods = ['GET'])
def getMesa(id):
    json = controladorMesa.showidMesa(id)
    return jsonify(json)

@app.route("/Mesa/<string:id>", methods = ['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = controladorMesa.updateMesa(id)
    return jsonify(json)

@app.route("/Mesa/<string:id>", methods = ['DELETE'])
def eliminarMesa(id):
    json = controladorMesa.deleteMesa(id)
    return jsonify(json)

@app.route("/Partido", methods = ['GET'])
def getPartidos():
    json = controladorPartido.showallPartido()
    return jsonify(json)

@app.route("/Partido", methods = ['POST'])
def crearPartido():
    data = request.get_json()
    json = controladorPartido.createPartido(data)
    return jsonify(json)

@app.route("/Partido/<string:id>", methods = ['GET'])
def getPartido(id):
    json = controladorPartido.showidPartido(id)
    return jsonify(json)

@app.route("/Partido/<string:id>", methods = ['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = controladorPartido.updatePartido(id)
    return jsonify(json)

@app.route("/Partido/<string:id>", methods = ['DELETE'])
def eliminarPartido(id):
    json = controladorPartido.deletePartido(id)
    return jsonify(json)

@app.route("/Resultado", methods = ['GET'])
def getResultado():
    json = controladorResultado.showallResultado()
    return jsonify(json)

@app.route("/Resultado/<string:id>", methods = ['GET'])
def getResultadoid(id):
    json = controladorResultado.showidResultado(id)
    return jsonify(json)

@app.route("/Resultado/Mesa/<string:idMesa>/Candidatos/<string:idCandidatos>", methods = ['POST'])
def crearResultadoMesaCandidato(idMesa, idCandidatos):
    data = request.get_json()
    json = controladorResultado.createResultado(data, idMesa, idCandidatos)
    return jsonify(json)

@app.route("/Resultado/<string:idR>/Mesa/<string:idM>/Candidatos/<string:idC>", methods = ['PUT'])
def modificarResultados(idR, idM, idC):
    data = request.get_json()
    json = controladorResultado.updateResultado(idR, data, idM, idC)
    return jsonify(json)

@app.route("/Resultado/<string:id>", methods = ['DELETE'])
def eliminarResultado(id):
    json = controladorResultado.deleteResultado(id)
    return jsonify(json)

@app.route("/Resultado/Candidato/<string:idC>", methods = ['GET'])
def inscritosEnCandidatos(idC):
    json = ControladorResultado.listarresultadoscandidato(idC)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host = dataConfig["url-backend"], port = dataConfig["port"])