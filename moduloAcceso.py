# -*- coding: utf-8 -*-
from pexpect import pxssh
from time import time

def ssh():
    start_time = time()
    value      = 0
    recibido   = 0
    enviado    = 0
    conexiones = 0
    ssh_servidor = '10.0.0.19'
    ssh_usuario  = 'daniela'
    ssh_clave    = 'password'

    # Comandos que vamos a ejecutar en el servidor

    trafico_recibido        = 'snmpget -v2c -c sshgroup localhost 1.3.6.1.2.1.4.3.0'
    trafico_enviado         = 'snmpget -v2c -c sshgroup localhost 1.3.6.1.2.1.4.9.0'
    conexiones_establecidas = 'snmpget -v2c -c sshgroup localhost 1.3.6.1.2.1.6.9.0'
    len_comando = len(trafico_recibido)

    try:
        s = pxssh.pxssh()

        if not s.login (ssh_servidor, ssh_usuario, ssh_clave):
               value = 33

        else:
            value = 100

            s.sendline (trafico_recibido)
            s.prompt()         # match the prompt
            recibido = str(s.before)
            recibido = recibido[(len_comando+39):(len(recibido)-5)]

            s.sendline(trafico_enviado)
            s.prompt()  # match the prompt
            enviado = str(s.before)
            enviado = enviado[(len_comando + 39):(len(enviado) - 5)]

            s.sendline(conexiones_establecidas)
            s.prompt()  # match the prompt
            conexiones = str(s.before)
            conexiones = conexiones[(len_comando + 37):(len(conexiones) - 5)]

            s.logout()
    except:
        value = 33

    elapsed_time = time() - start_time
    return recibido,enviado,conexiones,value, elapsed_time





