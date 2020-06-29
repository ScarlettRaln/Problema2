from inicio import primermodulo
from moduloArchivo import conexion_ftp
from graficar import graficar
from moduloAcceso import ssh

rrdpath = '/home/scarlett/Escritorio/Redes_3/P2/RRD/'
imgpath = '/home/scarlett/Escritorio/Redes_3/P2/IMG/'

comunidad = "CarlaGonzalez4cv5"
host = "localhost"

resp = 'Y'

while resp != 'N':
    print("**************************************************************")
    print("*                         Problema 2                         *")
    print("*                Administración de rendimiento               *")
    print("**************************************************************\n")

    print("    1.- Inicio")  # Solo falta lo del HD
    print("    2.- Información") # LISTO!
    print("    3.- Archivos")  # LISTO!
    print("    4.- Acceso")  # LISTO!
    print("    5.- DNS")
    print("    6.- Correo")
    print("    7.- Obtener Reporte\n")

    numero = int(input("Seleccione una opcion: "))

    if numero == 1:
        print("    1.- Inicio")
        # Este módulo nos ejecuta un hilo en el que nos recaba información para realizar las gráficas
        primermodulo(comunidad, host)

# ------ Servidor de Información ------

    if numero == 2:

        valor, byte_recv, ancho_bnda, tiempo = http()

        if valor == 100:
            print("         HTTP session login successful    ")
            print("    >> Bytes recibidos: " + str(byte_recv))
            print("    >> Ancho de banda: " + str(ancho_bnda) + "Mbps")
            print("    >> Tiempo de respuesta del servidor: %0.2f seg" % tiempo)

        if valor == 33:
            print("    >> Status del Servidor de Información: DOWN D:")

# ------ Servidor de Archivos ------

    if numero == 3:
        reqst = ""

        inf, elapsed_time, reqst = conexion_ftp()

        print("    >> Tiempo de respuesta del servidor: %0.2f segundos." % elapsed_time)

        if inf == 100:
            print("         FTP session login successful    ")
            print("    >> Respuesta de Bienvenida del Servidor: " + reqst)
        if inf == 33:
            print("    >> Status del Servidor de Archivos: DOWN D:")

# ------ Servidor de Acceso ------

    if numero == 4:
        print("    4.- Acceso")
        trafico_recv, trafico_env, conn, inf, time_ = ssh()

        if inf == 100:
            print("         SSH session login successful    ")
            print("    >> Tráfico recibido: " + trafico_recv)
            print("    >> Tráfico enviado: " + trafico_env)
            print("    >> Conexiones establecidas: " + conn)
            print("    >> Tiempo de actividad de la conexión: %0.2f seg" % time_)

        if inf == 33:
            print("    >> Status del Servidor de Acceso: DOWN D:")

# ------ Servidor de DNS ------

    if numero == 5:
        print("    5.- DNS")

# ------ Servidor de Correo ------

    if numero == 6:
        print("    6.- Correo")

    if numero == 7:
        print("    7.- Obtener Reporte\n")

        graficar(rrdpath, imgpath)

    resp = str(input("\n                   ¿Regresar al Menú?[Y/N] "))
    resp = resp.upper()
