# CLASE AVION
# AUTORES: JHONEYKER DELGADO, EMMANUEL VALENCIA, SIMON GUARIN, CAMILO MIRANDA Y JACOBO LEAL.
import math
from gestorAplicacion.hangar.Aeronave import Aeronave
from gestorAplicacion.hangar.Silla import Silla
from gestorAplicacion.hangar.Clase import Clase
from gestorAplicacion.hangar.Ubicacion import Ubicacion
#from gestorAplicacion.adminVuelos import *

class Avion(Aeronave):
    _NUM_SILLAS_ECONOMICAS = 24
    _NUM_SILLAS_EJECUTIVAS = 12

    # CONSTRUCTOR
    def __init__(self, nombre, aerolinea=None):
        super().__init__(nombre, aerolinea)


    def getNombre(self):
        texto = super().getNombre() + "_A"
        return texto

    @staticmethod
    def getNumSillasEconomicas():
        return Avion._NUM_SILLAS_ECONOMICAS

    @staticmethod
    def getNumSillasEjecutivas():
        return Avion._NUM_SILLAS_EJECUTIVAS

    # METODOS

    #	ESTE METODO RECIBE UN TIPO DE DATO DOUBLE DE LA DISTANCIA QUE HAY DESDE EL LUGAR DE ORIGEN AL LUGAR DE DESTINO
    #	Y RETONARNA EL COSTO TOTAL DE GASOLINA PARA RECORRER EL TRAYECTO
    def Calcular_Consumo_Gasolina(self, distancia_en_km):
        consumido = None
        consumido = self.getGastoGasolina() * distancia_en_km
        return consumido