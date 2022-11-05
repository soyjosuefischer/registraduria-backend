from Modelos.modeloResultadoPartido import ModeloResultadoPartido
from Repositorio.InterfaceRepositorio import InterfaceRepositorio
from bson import ObjectId

class RepositorioResultadoPartido(InterfaceRepositorio[ModeloResultadoPartido]):
    def getlistResultadosPartido(self,idP):
        laquery = {"Partido.$id": ObjectId(idP)}
        return self.query(laquery)

    # def getmesamayorparticipacion(self):

    # def getpartidomayorparticipacion(self):