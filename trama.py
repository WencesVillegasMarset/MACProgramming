import numpy as np

class Trama(object):

    def __init__(self, tipo=None, mac_origen=[0,1], mac_destino=[1,0]):
        self.mac_origen = mac_origen
        self.mac_destino = mac_destino
        if tipo == 'control':
            self.tipo = 1
        else:
            self.tipo = 0
            self.payload = _generar_payload()
            self.suma = dec2bin(self.checksum(payload=self.payload))

        self.inicio = [0,1,1,1,1,1,0]
        self.fin = [0,1,1,1,1,1,0]

    def checksum(self, payload = None):
        if payload:
            return sum(payload)

    def get_representation(self):
        return self.inicio + self.mac_origen + self.mac_destino + self.payload + self.suma + self.fin

def _generar_payload():
    return [np.random.randint(0,2) for x in range(np.random.randint(100,1000))]

def dec2bin(decimal):
    return [int(binary) for binary in "{0:b}".format(decimal)]
        
if __name__ == "__main__":
    trama = Trama(tipo='datos')
    print(trama.get_representation())
