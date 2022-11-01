from Modelos.modeloPartido import ModeloPartido
from Repositorio.RepositorioPartido import RepositorioPartido

class ControladorPartido():
    def __init__(self):
        print("Creando el controlador de Partido")
        self.repositorioPartido = RepositorioPartido()

    def createPartido(self, infoPartido):
        print("Creando el partido...")
        nuevopartido = ModeloPartido(infoPartido)
        print("Partido a crear en base de datos: ", nuevopartido.__dict__)
        self.repositorioPartido.save(nuevopartido)
        return True

    def showidPartido(self, id):
        print("Mostrando un Partido con su ID ", id)
        partido=ModeloPartido(self.repositorioPartido.findById(id))
        return partido.__dict__

    def showallPartido(self):
        print("Mostrando todos los partidos de la base de datos ")
        return self.repositorioPartido.findAll()

    def updatePartido(self,infoPartido):
        partidoactual = ModeloPartido(self.repositorioPartido.findById((infoPartido["infoPartido"])))
        print("Actualizando Partido con su ID ", partidoactual)
        partidoactual.nombre = infoPartido["nombre"]
        partidoactual.lema = infoPartido["lema"]
        self.repositorioPartido.save(partidoactual)
        return True

    def deletePartido(self, id):
        print("Eliminando Partido con su ID ", id)
        self.repositorioPartido.delete(id)
        return True