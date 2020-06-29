# -*- coding: utf-8 -*-
from ftplib import FTP
from time import time


def conexion_ftp():
    start_time = time()
    try:
        ftp = FTP()
        ftp.connect('10.0.0.8', 21, -999)
        ftp.login('omar', 'password')
        mns_bienvenida = str(ftp.getwelcome())

        if mns_bienvenida != " ":
            value = 100
            elapsed_time = time() - start_time

        ftp.close()

    except:
        value = 33
        elapsed_time = time() - start_time

    return value, elapsed_time, mns_bienvenida
