from Modelos.modeloMesa import ModeloMesa
from Repositorio.RepositorioMesa import RepositorioMesa


class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    def createMesa(self, infoMesa):
        nuevomesa = ModeloMesa(infoMesa)
        return self.repositorioMesa.save(nuevomesa)

    def showidMesa(self, id):
        mesa = ModeloMesa(self.repositorioMesa.findById(id))
        return mesa.__dict__

    def showallMesa(self):
        return self.repositorioMesa.findAll()

    def updateMesa(self, id, infoMesa):
        mesaactual = ModeloMesa(self.repositorioMesa.findById(id))
        mesaactual.numero = infoMesa["numero"]
        mesaactual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaactual)

    def deleteMesa(self, id):
        return self.repositorioMesa.delete(id)
