from Modelos.modeloPartido import ModeloPartido
from Modelos.modeloMesa import ModeloMesa
from Modelos.modeloResultadoPartido import ModeloResultadoPartido
from Repositorio.RepositorioPartido import RepositorioPartido
from Repositorio.RepositorioMesa import RepositorioMesa
from Repositorio.RepositorioResultadoPartido import RepositorioResultadoPartido
from bson import ObjectId

class ControladorResultadoPartido():
    def __init__(self):
        self.repositorioResultadoPartido = RepositorioResultadoPartido()
        self.repositorioPartido = RepositorioPartido()
        self.repositorioMesa = RepositorioMesa()

    def createResultado(self, infoResultado, idM, idP):
        elresultado = ModeloResultadoPartido(infoResultado)
        lamesa = ModeloMesa(self.repositorioMesa.findById(idM))
        elpartido = ModeloPartido(self.repositorioPartido.findById(idP))
        elresultado.mesa = lamesa
        elresultado.partido = elpartido
        return self.repositorioResultadoPartido.save(elresultado)

    def showidResultado(self, id):
        resultado = ModeloResultadoPartido(
            self.repositorioResultadoPartido.findById(id))
        return resultado.__dict__

    def showallResultado(self):
        return self.repositorioResultadoPartido.findAll()

    def updateResultado(self, idR, idM, idP, infoResultado):
        resultadoactual = ModeloResultadoPartido(self.repositorioResultadoPartido.findById(idR))
        lamesa = ModeloMesa(self.repositorioMesa.findById(idM))
        elpartido = ModeloPartido(self.repositorioPartido.findById(idP))
        resultadoactual.mesa = lamesa
        resultadoactual.partido = elpartido
        resultadoactual.numero_votos = infoResultado["numero_votos"]
        return self.repositorioResultadoPartido.save(resultadoactual)

    def deleteResultado(self, id):
        return self.repositorioResultadoPartido.delete(id)

    def listarresultadoscandidato(self, id):
        return self.repositorioResultadoPartido.getlistResultadosCandidato(id)