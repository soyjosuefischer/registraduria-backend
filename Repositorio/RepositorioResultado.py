from Modelos.modeloResultado import ModeloResultado
from Repositorio.InterfaceRepositorio import InterfaceRepositorio
from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[ModeloResultado]):
    def getlistResultadosCandidato(self, idC):
        laquery = {"Candidato.$id": ObjectId(idC)}
        return self.query(laquery)