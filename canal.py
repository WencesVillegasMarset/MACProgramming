import numpy as np
import estacion
class Canal(object):
    def __init__(self):
        self.tasa_errores = 0.1
        self.retraso = 0.1
        self.probabilidad_perdida = 0.05
        