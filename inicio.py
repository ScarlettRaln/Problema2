from getSNMP import consultaSNMP
import time
import threading
import rrdtool
import os
rrdpath = '/home/scarlett/Escritorio/Redes_3/P2/RRD/'


def primermodulo(comunidad, host):

    print("\n****************************************************")
    print("*                    = Inicio =                    *")
    print("****************************************************\n")

    SistemaOperativo = ""
    NumInterfaces = 0

    try:
        SistemaOperativo = str(consultaSNMP(comunidad, host, '1.3.6.1.2.1.1.1.0'))
        print("   > Sistema Operativo del Servidor: " + SistemaOperativo)

        NumInterfaces = consultaSNMP(comunidad, host, '1.3.6.1.2.1.2.1.0')
        print("   > Numero de Interfaces: " + NumInterfaces)

        #Para ver cuantos procesadores hay
        #snmpwalk -v2c -c CarlaGonzalez4cv5 localhost 1.3.6.1.2.1.25.3.3.1.2
    except:

        print("\n   > Agente desactivado")

    try:
        # SE CREAN LAS BASES DE DATOS

        ret = rrdtool.create(rrdpath + "CpuLoad1.rrd", "--start", 'N', "--step", '60', "DS:CPUload1:GAUGE:600:U:U", "RRA:AVERAGE:0.5:1:24")
        if ret:
            print(rrdtool.error())

        ret = rrdtool.create(rrdpath + "CpuLoad2.rrd", "--start", 'N', "--step", '60', "DS:CPUload2:GAUGE:600:U:U", "RRA:AVERAGE:0.5:1:24")
        if ret:
            print(rrdtool.error())

        ret = rrdtool.create(rrdpath + "RAMUsed.rrd", "--start", 'N', "--step", '60', "DS:RAMUsed:GAUGE:600:U:U", "RRA:AVERAGE:0.5:1:24")
        if ret:
            print(rrdtool.error())
    except:
        print("\n   > Problemas para crear las BD")

    try:
        #VAMOS A INICIAR EL HILO
        threads = []
        t = threading.Thread(target=worker, args=(comunidad, host))
        threads.append(t)
        t.start()
    except:
        print("\n   > Problemas para iniciar el hilo")

def worker(comunidad, host): #Hilo para realizar las consultas constantes de los valores
    Total_RAM = 0
    porcentaje = 0
    Total_RAM = int(consultaSNMP(comunidad, host, '1.3.6.1.4.1.2021.4.5.0'))
    #print("Total_RAM: " + str(Total_RAM))

    # WHILE INFINITO PARA SOLICITAR INFORMACIÓN Y ACTUALIZAR
    while 1:
        carga_CPU1 = 0
        carga_CPU2 = 0
        used_Ram = 0
        # Información del CPU

        carga_CPU1 = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.25.3.3.1.2.196608'))
        valor = "N:" + str(carga_CPU1)
        rrdtool.update(rrdpath + "CpuLoad1.rrd", valor)
        rrdtool.dump(rrdpath + "CpuLoad1.rrd", rrdpath + "CpuLoad1.xml")
        time.sleep(1)

        carga_CPU2 = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.25.3.3.1.2.196609'))
        valor = "N:" + str(carga_CPU2)
        rrdtool.update(rrdpath + "CpuLoad2.rrd", valor)
        rrdtool.dump(rrdpath + "CpuLoad2.rrd", rrdpath + "CpuLoad2.xml")
        time.sleep(1)

        used_Ram = int(consultaSNMP(comunidad, host, '1.3.6.1.4.1.2021.4.11.0'))
        porcentaje = int((used_Ram *100)/Total_RAM)
        #print("Total = "+ str(Total_RAM) + "    USADA: "+ str(used_Ram)+ "    PORCENTAJE: "+ str(porcentaje))
        valor = "N:" + str(porcentaje)
        rrdtool.update(rrdpath + "RAMUsed.rrd", valor)
        rrdtool.dump(rrdpath + "RAMUsed.rrd", rrdpath + "RAMUsed.xml")
        time.sleep(1)

    if ret:
        print(rrdtool.error())
        time.sleep(300)

