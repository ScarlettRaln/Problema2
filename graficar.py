import rrdtool

def graficar(rrdpath,imgpath):
    print("\n *****************************************")
    print(" *       = Generación de Gráficas =       *")
    print(" *****************************************\n")

    ultima_lectura = int(rrdtool.last(rrdpath + "CpuLoad1.rrd"))
    tiempo_final = ultima_lectura
    tiempo_inicial = tiempo_final - 600

    ret1 = rrdtool.graph(imgpath + "CPU1.png",
                        "--start", str(tiempo_inicial),
                        "--end", str(tiempo_final),
                        "--vertical-label=Carga CPU 1",
                        "--title=Uso de CPU1",
                        "--color", "ARROW#009900",
                        '--vertical-label', "Uso de CPU1 (%)",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        "DEF:carga1=" + rrdpath + "CpuLoad1.rrd:CPUload1:AVERAGE",
                        "CDEF:umbral70=carga1,70,LT,0,carga1,IF",
                        "VDEF:carga1MAX=carga1,MAXIMUM",
                        "VDEF:carga1MIN=carga1,MINIMUM",
                        "VDEF:carga1STDEV=carga1,STDEV",
                        "VDEF:carga1LAST=carga1,LAST",
                        "AREA:carga1#00FF00:Carga del CPU 1",
                        "AREA:umbral70#FF9F00:Tráfico de carga mayor que 70",
                        "HRULE:90#FF0000:Umbral 3 - 90%",
                        "HRULE:80#FFAA00:Umbral 2 - 80%",
                        "HRULE:70#CCFF00:Umbral 1 - 70%",
                        "PRINT:carga1MAX:%6.2lf %S",
                        "GPRINT:carga1MIN:%6.2lf %SMIN",
                        "GPRINT:carga1STDEV:%6.2lf %SSTDEV",
                        "GPRINT:carga1LAST:%6.2lf %SLAST")

    ultimo_valor1 = float(ret1[0])

    ret2 = rrdtool.graphv(imgpath + "CPU2.png",
                          "--start", str(tiempo_inicial),
                          "--end", str(tiempo_final),
                          "--title", "Carga de CPU 2",
                          "--vertical-label=Uso de CPU (%)",
                          '--lower-limit', '0',
                          '--upper-limit', '100',
                          "DEF:carga2=" + rrdpath + "CpuLoad2.rrd:CPUload2:AVERAGE",
                          "CDEF:umbral70=carga2,70,LT,0,carga2,IF",
                          "VDEF:carga2MAX=carga2,MAXIMUM",
                          "VDEF:carga2MIN=carga2,MINIMUM",
                          "VDEF:carga2STDEV=carga2,STDEV",
                          "VDEF:carga2LAST=carga2,LAST",
                          "AREA:carga2#00FF00:Carga del CPU 2",
                          "AREA:umbral70#FF9F00:Tráfico de carga mayor que 70",
                          "HRULE:90#FF0000:Umbral 3 - 90%",
                          "HRULE:80#FFAA00:Umbral 2 - 80%",
                          "HRULE:70#CCFF00:Umbral 1 - 70%",
                          "PRINT:carga2MAX:%6.2lf %S",
                          "GPRINT:carga2MIN:%6.2lf %SMIN",
                          "GPRINT:carga2STDEV:%6.2lf %SSTDEV",
                          "GPRINT:carga2LAST:%6.2lf %SLAST")

    ultimo_valor2 = float(ret2['print[0]'])

    ret_ram = rrdtool.graphv(imgpath + "Ram_Used.png",
                             "--start", str(tiempo_inicial),
                             "--end", str(tiempo_final),
                             "--title", "Memoria Ram utilizada",
                             "--vertical-label=Uso de la RAM (%)",
                             '--lower-limit', '0',
                             '--upper-limit', '100',
                             "DEF:cargaRam=" + rrdpath + "RAMUsed.rrd:RAMUsed:AVERAGE",
                             "CDEF:umbral70=cargaRam,70,LT,0,cargaRam,IF",
                             "VDEF:cargaRamMAX=cargaRam,MAXIMUM",
                             "VDEF:cargaRamMIN=cargaRam,MINIMUM",
                             "VDEF:cargaRamSTDEV=cargaRam,STDEV",
                             "VDEF:cargaRamLAST=cargaRam,LAST",
                             "AREA:cargaRam#00FF00:Uso de la RAM",
                             "AREA:umbral70#FF9F00:Tráfico de carga mayor que 70",
                             "HRULE:90#FF0000:Umbral 3 - 90%",
                             "HRULE:80#FFAA00:Umbral 2 - 80%",
                             "HRULE:70#CCFF00:Umbral 1 - 70%",
                             "PRINT:cargaRamMAX:%6.2lf %S",
                             "GPRINT:cargaRamMIN:%6.2lf %SMIN",
                             "GPRINT:cargaRamSTDEV:%6.2lf %SSTDEV",
                             "GPRINT:cargaRamLAST:%6.2lf %SLAST")

    ultimo_valorRAM = float(ret_ram['print[0]'])

    print(str(ultimo_valor1) + " : " + str(ultimo_valor2) + " : " + str(ultimo_valorRAM))
