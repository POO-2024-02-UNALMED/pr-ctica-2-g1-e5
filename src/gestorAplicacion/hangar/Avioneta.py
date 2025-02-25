# CLASE AVIONETA
# AUTORES: JHONEYKER DELGADO, EMMANUEL VALENCIA, SIMON GUARIN, CAMILO MIRANDA Y JACOBO LEAL.
import math
from .Aeronave import Aeronave
from .Silla import Silla
from .Clase import Clase
from .Ubicacion import Ubicacion

class Avioneta(Aeronave):

    _NUM_SILLAS_ECONOMICAS = 6
    _NUM_SILLAS_EJECUTIVAS = 4

    def __init__(self, nombre, aerolinea=None):
        super().__init__(nombre, aerolinea)
        super().asignarParamatrosSilla(self,2)
        

    @staticmethod
    def getNumSillasEconomicas():
        return Avioneta._NUM_SILLAS_ECONOMICAS

    @staticmethod
    def getNumSillasEjecutivas():
        return Avioneta._NUM_SILLAS_EJECUTIVAS

    #
    #	 * Este método recorreran los arreglos de sillas ejecutivos y economicas de cada
    #	 * avión y avioneta
    #	 * para verificar la cantidad de sillas que estan ocupadas y retornaran dicha
    #	 * cantidad
    #
    def Calcular_Sillas_Ocupadas(self):
        cont = 0
        for i in self.getSILLASECONOMICAS():
            if i.isEstado():
                cont += 1
        for j in self.getSILLASEJECUTIVAS():
            if j.isEstado():
                cont += 1
        return "Sillas ocupadas en la avioneta"+cont

    #
    #	 * Este método recibe un tipo de dato double de la distancia que hay desde el
    #	 * lugar de origen al lugar de destino
    #	 * y retornara el costo total de gasolina por recorrer el trayecto
    #

    def Calcular_Consumo_Gasolina(self, distancia_en_km):
        consumido = Aeronave.Gasto_gasolina * distancia_en_km
        return consumido
