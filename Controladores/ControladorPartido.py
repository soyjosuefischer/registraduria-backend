from Modelos.modeloPartido import ModeloPartido
from Repositorio.RepositorioPartido import RepositorioPartido

class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()

    def createPartido(self, infoPartido):
        nuevopartido = ModeloPartido(infoPartido)
        return self.repositorioPartido.save(nuevopartido)

    def showidPartido(self, id):
        partido=ModeloPartido(self.repositorioPartido.findById(id))
        return partido.__dict__

    def showallPartido(self):
        return self.repositorioPartido.findAll()

    def updatePartido(self, id, infoPartido):
        partidoactual = ModeloPartido(self.repositorioPartido.findById(id))
        partidoactual.nombre = infoPartido["nombre"]
        partidoactual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoactual)

    def deletePartido(self, id):
        return self.repositorioPartido.delete(id)