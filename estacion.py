from queue import Queue
from trama import Trama

class Estacion(object):

    def __init__(self, direccion_mac):
        self.buffer_size = 5
        self.buffer = Queue(self.buffer_size)
        self.direccion_mac = direccion_mac

    def send(self, direccion_destino):
        self._recibir_desde_red()
        self._encapsular_paquete()
        return Trama(tipo='datos', mac_origen=self.direccion_mac, mac_destino=direccion_destino)

    def recieve(self, trama_entrante):
        self.buffer.put(trama_entrante)
        print('Recibido por ' + str(self.direccion_mac))

    def process(self):
        trama = self.buffer.get()
        if((trama.checksum(trama.payload)) != trama.checksum):
            print('Errores detectados')
        

    def ack(self):
        ack = Trama(tipo='control', mac_origen=self.direccion_mac)
        return ack

    def _recibir_desde_red(self):
        print('Paquete recibido desde Red')

    def _encapsular_paquete(self):
        print('Encapsulando Paquete: Generando Trama')
        return Trama(tipo='datos', mac_origen=self.direccion_mac)

    def entregar_a_red(self):
        print('Paquete entregado a red')

    def _desencapsular_trama(self):
        print('Trama desencapsulada')

    def getDireccionMAC(self):
        return self.direccion_mac

