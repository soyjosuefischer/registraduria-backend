from Modelos.modeloCandidato import ModeloCandidato
from Modelos.modeloPartido import ModeloPartido
from Repositorio.RepositorioCandidato import RepositorioCandidato
from Repositorio.RepositorioPartido import RepositorioPartido

class ControladorCandidato():
    def __init__(self):
        print("Creando el controlador de Candidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def createCandidato(self, infoCandidato):
        nuevoCandidato = ModeloCandidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def showidCandidato(self, id):
        return self.repositorioCandidato.findById(id)

    def showallCandidato(self):
        return self.repositorioCandidato.findAll()

    def updateCandidato(self, id, infoCandidato):
        candidatoactual = ModeloCandidato(self.repositorioCandidato.findById(id))
        print("Actualizando el Candidato con ID ", candidatoactual)
        candidatoactual.cedula = infoCandidato["cedula"]
        candidatoactual.numero_resolucion = infoCandidato["numero_resolucion"]
        candidatoactual.nombre = infoCandidato["nombre"]
        candidatoactual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoactual)

    def deleteCandidato(self, id):
        return self.repositorioCandidato.delete(id)

    def asigPartido(self,idC, idP):
        candidatoactual = ModeloCandidato(self.repositorioCandidato.findById(idC))
        partidoactual = ModeloPartido(self.repositorioPartido.findById(idP))
        candidatoactual.partido = partidoactual
        print("Candidato a asignar a un partido: ", candidatoactual.__dict__)
        self.repositorioCandidato.save(candidatoactual)
        return True