import requests
from time import time
from getSNMP import consultaSNMP

comunidad = 'httpgroup'
host = '10.0.0.21'

def http():
    value = 0
    ancho = 0
    recibidos = 0
    start_time = time()
    try:
        #Realizamos una solicitud para conectarnos con el servidor :3
        response = requests.get('http://10.0.0.21/capital-humano.html')
        respuesta = str(response)
        if(respuesta == "<Response [200]>"):
            elapsed_time = time() - start_time
            value = 100

            recibidos = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.2.2.1.10.2'))
            ancho_banda = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.2.2.1.5.2'))
            # 1Megabit = 1000000 bits
            ancho = ancho_banda / 1000000
        else:
            value = 33

    except:
        value = 33
        elapsed_time = time() - start_time

    return value, recibidos, ancho, elapsed_time
