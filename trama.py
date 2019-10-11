import numpy as np
from bitarray import bitarray
class Trama(object):

    def __init__(self, tipo=None, mac_origen=None, mac_destino=None):
        self.mac_origen = mac_origen
        self.mac_destino = mac_destino

        if tipo == 'control':
            self.tipo = 'ACK'
        else:
            self.payload = _generar_payload()
        self.suma = self.payload.count()

    def checksum(self, payload = None):
        if payload:
            return sum(payload.tolist())
    def generate_checksum(self):
        pass

def _generar_payload():
    payload_lenght = np.random.randint(100, 1000)
    return bitarray(payload_lenght)
        
if __name__ == "__main__":
    trama = Trama()
