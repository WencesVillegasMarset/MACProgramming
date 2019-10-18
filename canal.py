import numpy as np
from estacion import Estacion
from trama import Trama
from time import sleep

class Canal(object):
    def __init__(self):
        self.tasa_errores = 0.1
        self.retraso = 0.1
        self.probabilidad_perdida = 0.05
        self.estacion_1 = Estacion([0,1])
        self.estacion_2 = Estacion([1,0])

    def envio(self, origen=None, destino=None):
        trama = (origen.send(destino.direccion_mac))
        trama = self.transferencia(trama)
        destino.recieve(trama)
        destino.process()
        

    def transferencia(self, trama):
        print('Enviando por enlace')
        sleep(self.retraso*10)
        if(np.random.random()< self.probabilidad_perdida):
            trama = None 
            print('Trama perdida')   
        if(np.random.random()< self.tasa_errores):
            if(trama.payload):
                trama.payload = self.generar_errores(trama.payload)
                print('errores generados')
        return trama
        
    def generar_errores(self, payload):
        return [np.random.randint(0,2) if np.random.random() < 0.3 else x for x in payload]

if __name__ == "__main__":
    trama = Trama()
    canal = Canal()
