from queue import Queue
from trama import Trama
from canal import Canal
import time
import numpy as np
class Estacion(object):

    def __init__(self, direccion_mac):
        self.buffer_size = 5
        self.buffer = Queue(self.buffer_size)
        self.direccion_mac = direccion_mac
        self.canal = Canal.getInstance()
        self.ultima_trama = None
        # self.enviar = False

    def send(self, estacion_destino):
        '''
        Pasos necesarios para poder enviar una trama al destino
        '''
        self.getCanal()
        self._recibir_desde_red()
        trama = self._encapsular_paquete(estacion_destino.direccion_mac)
        self.ultima_trama = trama # en caso de ser necesario reenvio, recordar
        self.canal.envio(trama, self, estacion_destino)
        self.canal.liberarCanal()

    def recieve(self, trama_entrante, origen):
        '''
        Pasos que la estacion hace al recibir una trama de cualquier tipo
        '''
        self.buffer.put(trama_entrante)
        print('Recibido por ' + str(self.direccion_mac))
        is_ok, trama = self.process()
        if is_ok:
            if trama.tipo == 'datos': # todo ok, enviar ack
                self.canal.envio(self.ack(), self, origen)
                self.entregar_a_red()
            if trama.tipo == 'nak': # reenvia la ultima trama
                self.canal.envio(self.ultima_trama, self, origen)
        else:
            self.canal.envio(self.nak(), self, origen) # todo mal, enviar nak

    def getCanal(self):
        '''
        Funcion para obtener un canal, si esta ocupado vuelve a intentar en un tiempo random de 0 a 5 seg
        '''
        while True:
            if self.canal.checkOcupado():
                time.sleep(np.random.random() * 5)
            else:
                self.canal.ocuparCanal()
                print('----------------> CANAL OCUPADO POR ' + str(self.direccion_mac)+ '\n')
                break

    def process(self):
        '''
        Funcion para procesar una trama en buffer
        returns : boolean , Trama
        SI errores => False
        else => True
        '''
        try:
            trama = self.buffer.get()
        except Exception: # buffer vacio o error en lectura 
            print('Exception, terminate script')
            exit()
        if trama is None: # trama perdida en la transferencia
            return False , trama
        print('Procesando!' + ' TIPO:' + trama.tipo)
        if (trama.tipo == 'datos'): # checkeo de errores
            if((trama.checksum(trama.payload)) != trama.suma):
                print('ERROR EN CHECKSUM')
                return False, trama            
        return True, trama

    def ack(self):
        '''
        Genera trama ACK
        '''
        return Trama(tipo='ack', mac_origen=self.direccion_mac)

    def nak(self):
        '''
        Genera trama NAK
        '''
        return Trama(tipo='nak', mac_origen=self.direccion_mac)


    def _recibir_desde_red(self):
        print('Paquete recibido desde Red')

    def _encapsular_paquete(self, mac_destino):
        print('Encapsulando Paquete: Generando Trama')
        return Trama(tipo='datos', mac_origen=self.direccion_mac, mac_destino=mac_destino)

    def entregar_a_red(self):
        print('Paquete entregado a red')

    def _desencapsular_trama(self):
        print('Trama desencapsulada')

    def getDireccionMAC(self):
        return self.direccion_mac

