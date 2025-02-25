# CLASE AVION
# AUTORES: JHONEYKER DELGADO, EMMANUEL VALENCIA, SIMON GUARIN, CAMILO MIRANDA Y JACOBO LEAL.
import math
from .Aeronave import Aeronave
from .Silla import Silla
from .Clase import Clase
from .Ubicacion import Ubicacion
from .Terminal import Terminal

#from gestorAplicacion.adminVuelos import *

class Avion(Terminal,Aeronave):
    _NUM_SILLAS_ECONOMICAS = 24
    _NUM_SILLAS_EJECUTIVAS = 12

    # CONSTRUCTOR
    def __init__(self, nombre, aerolinea=None):
        super().__init__(nombre, aerolinea)
        super().asignarParamatrosSilla(self,1)


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
        consumido = Aeronave.Gasto_gasolina * distancia_en_km
        return consumido
