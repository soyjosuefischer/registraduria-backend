from Modelos.modeloMesa import ModeloMesa
from Repositorio.RepositorioMesa import RepositorioMesa

class ControladorMesa():
    def __init__(self):
        print("Creando el controlador de Mesa")
        self.repositorioMesa = RepositorioMesa()

    def createMesa(self, infoMesa):
        print("Creando mesa...")
        nuevomesa = ModeloMesa(infoMesa)
        print("Mesa a crear en la base de datos: ", nuevomesa.__dict__)
        self.repositorioMesa.save(nuevomesa)
        return True

    def showidMesa(self, id):
        print("Mostrando un Mesa con su ID ", id)
        mesa = ModeloMesa(self.repositorioMesa.findById(id))
        return mesa.__dict__

    def showallMesa(self):
        print("Mostrando todas las mesas de la base de datos ")
        return self.repositorioMesa.findAll()

    def updateMesa(self, infoMesa):
        mesaactual = ModeloMesa(self.repositorioMesa.findById((infoMesa["infoMesa"])))
        print("Actualizando Mesa con su ID ", mesaactual)
        mesaactual.numero = infoMesa["numero"]
        mesaactual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        self.repositorioMesa.save(mesaactual)
        return True

    def deleteMesa(self, id):
        print("Eliminando Mesa con su ID ", id)
        self.repositorioMesa.delete(id)
        return True