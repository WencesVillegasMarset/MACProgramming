import numpy as np

TRAMA_TYPES = ['control', 'nak', 'datos']


class Trama(object):
    def __init__(self, tipo=None, mac_origen=[0], mac_destino=[1]):
        if tipo not in TRAMA_TYPES:
            raise Exception()
        self.mac_origen = mac_origen
        self.mac_destino = mac_destino
        if tipo == 'ack':
            self.tipo = 'ack'
        if tipo == 'nak':
            self.tipo = 'nak'
        if tipo == 'datos':
            self.tipo = 'datos'
            self.payload = _generar_payload()
            self.suma = self.checksum(payload=self.payload)

        self.inicio = [0,1,1,1,1,1,0]
        self.fin = [0,1,1,1,1,1,0]

    def checksum(self, payload = None):
        '''
        Funcion simple de checksum, no es un checksum real
        '''
        if payload:
            return sum(payload)

    def get_representation(self):
        '''
        Devuelve la representacion completa de la trama, como una lista de binarios
        '''
        return self.inicio + self.mac_origen + self.mac_destino + self.payload + self.suma + self.fin

def _generar_payload():
    '''
    Genera una lista de 0s y 1s de longitud entre 100 y 1000 bits
    '''
    return [np.random.randint(0,2) for x in range(np.random.randint(100,1000))]

def dec2bin(decimal):
    '''
    Transforma un decimal a una lista de 0s y 1s
    '''
    return [int(binary) for binary in "{0:b}".format(decimal)]
        
if __name__ == "__main__":
    trama = Trama(tipo='datos')
    print(trama.get_representation())
