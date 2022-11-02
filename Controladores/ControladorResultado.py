from Modelos.modeloCandidato import ModeloCandidato
from Modelos.modeloMesa import ModeloMesa
from Modelos.modeloResultado import ModeloResultado
from Repositorio.RepositorioCandidato import RepositorioCandidato
from Repositorio.RepositorioMesa import RepositorioMesa
from Repositorio.RepositorioResultado import RepositorioResultado
from bson import ObjectId

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    def createResultado(self,infoResultado,idM,idC):
        elresultado = ModeloResultado(infoResultado)
        lamesa = ModeloMesa(self.repositorioMesa.findById(idM))
        elcandidato = ModeloCandidato(self.repositorioCandidato.findById(idC))
        elresultado.mesa = lamesa
        elresultado.candidato = elcandidato
        return self.repositorioResultado.save(elresultado)

    def showidResultado(self, id):
        resultado = ModeloResultado(self.repositorioResultado.findById(id))
        return resultado.__dict__

    def showallResultado(self):
        return self.repositorioResultado.findAll()

    def updateResultado(self, infoResultado,idM,idC):
        resultadoactual = ModeloResultado(self.repositorioResultado.findById(infoResultado))
        resultadoactual.numero_votos = infoResultado["numero_votos"]
        lamesa=ModeloMesa(self.repositorioMesa.findById(idM))
        elcandido=ModeloCandidato(self.repositorioCandidato.findById(idC))
        resultadoactual.mesa = lamesa
        resultadoactual.candidato = elcandido
        return self.repositorioResultado.save(resultadoactual)

    def deleteResultado(self, id):
        self.repositorioResultado.delete(id)
        return True

    def listarresultadoscandidato(self,idCa):
        return self.repositorioResultado.getlistResultadosCandidato(idCa)