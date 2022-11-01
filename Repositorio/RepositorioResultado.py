from Modelos.modeloResultado import modeloResultado
from Repositorio.InterfaceRepositorio import InterfaceRepositorio
from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[modeloResultado]):
    def getlistResultadosCandidato(self,idC):
        laquery = {"Candidato.$id": ObjectId(idC)}
        return self.query(laquery)

    # def getmesamayorparticipacion(self):

    # def getpartidomayorparticipacion(self):