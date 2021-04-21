import numpy as np
import os
from scripts.complejidad import complejidad
from scripts.bin_media import bin_media
from scripts.bin_mediana import bin_mediana
from scripts.detectar_maximos import detectar_maximos
from scripts.utils import printProgressBar
from scripts.binarizacion import binarizacion
from scripts.test_all import test_all


def main(crear_maximos, binarizar_archivos, test_estadistico):
    if crear_maximos:
        detectar_maximos('./datos/21-4-7/20210407-0009',60,0.05,0.01)
    if binarizar_archivos:
        binarizacion()
    if test_estadistico:
        test_all()
    


if __name__ == "__main__":
    complejidad([0,1])
    main(False,False,True) 
