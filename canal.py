import numpy as np
from trama import Trama
from time import sleep

      
         
class Canal(object):
    __instance = None

    @staticmethod 
    def getInstance():
        
        if Canal.__instance == None:
            Canal()
        return Canal.__instance

    def __init__(self):
        if Canal.__instance != None:
         raise Exception("Singleton!")
        else:
            self.tasa_errores = 0.30
            self.retraso = 0.05
            self.probabilidad_perdida = 0.05
            self.ocupado = False
            Canal.__instance = self

    def checkOcupado(self):
        return self.ocupado

    def ocuparCanal(self):
        self.ocupado = True
    
    def liberarCanal(self):
        self.ocupado = False
        

    def envio(self, trama, origen, destino):
        '''
        Se encarga de recibir la trama y hacerla llegar al destino
        '''
        trama = self.transferencia(trama)
        destino.recieve(trama, origen)
            

    def transferencia(self, trama):
        '''
        Simula la transferencia de la trama a traves del canal
        La trama puede perderse o dañarse
        '''
        sleep(self.retraso*10) # simula retardo de propagacion
        #solo se pierden las tramas de datos por que sino re largo
        if trama.tipo == 'datos': 
            if(np.random.random() < self.probabilidad_perdida): 
                print('Trama perdida') 
                return None # se pierde la trama
            if(np.random.random() < self.tasa_errores): 
                if(trama.payload is not None): 
                    trama.payload = self.generar_errores(trama.payload) # intercambia ceros con unos 
                    print('errores generados')
        return trama

    def generar_errores(self, payload):
        '''
        Genera una nueva payload a partir de la original, con una probabilidad de 0,3 de regenerar cada bit
        '''
        return [np.random.randint(0,2) if np.random.random() < 0.3 else x for x in payload]


