from canal import Canal
import numpy as np
import threading
import time
from estacion import Estacion

estacion_1 = Estacion(0)
estacion_2 = Estacion(1)

# funcion para ejecutar cada estacion

def estacion(index):
    #depende el indice que se pasa, quien es origen y quien es destino
    if index == 1:
        origen = estacion_1
        destino = estacion_2
    else:
        origen = estacion_2
        destino = estacion_1
    
    for i in range(30):
        origen.send(destino)
        time.sleep(np.random.random() * 10)
if __name__ == "__main__":
    # creamos un hilo para cada estacion
    #estacion(1)
    threads = list()
    for index in range(2):
        x = threading.Thread(target=estacion, args=(index,))
        threads.append(x)
        x.start()
