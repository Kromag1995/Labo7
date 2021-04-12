import numpy as np
import os
from .complejidad import complejidad
from .bin_media import bin_media
from .bin_mediana import bin_mediana
from .utils import printProgressBar


def binarizacion():
    resultados_Complejidad = "Nombre del Archivo;Longitud de la cadena;Media;Complejidad_Media;Mediana;Complejidad_Mediana \n"
    for dirpath,dirname, files in os.walk('./maximos/Nobinarizados'):
        l = len(files)
        printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for k,archivo in enumerate(files):
            maximos = np.loadtxt(dirpath+'/'+archivo)  # Carga la serie de maximos de un archivo
            if ('t' in archivo): # Si estoy el t de los maximos tengo que calcular la diferencia temporal
                def_temp = []
                for i in range(1,len(maximos)):
                    def_temp.append(maximos[i]-maximos[i-1])
                maximos = def_temp[:]
                del(def_temp)
            binarios_media,media = bin_media(maximos) #Binarizo la serie
            binarios_mediana,mediana = bin_mediana(maximos)
            archivo = archivo.replace(".bin", "") 
            output_file = open(f'maximos/Binarizados/{archivo}_media_{len(binarios_media)}.bin', 'w') # Guardo las serie binarizadas
            stingbin = ''.join([str(num) for num in binarios_media])
            output_file.write(stingbin)
            output_file.close()
            output_file = open(f'maximos/Binarizados/{archivo}_mediana{len(binarios_mediana)}.bin', 'w')
            stingbin = ''.join([str(num) for num in binarios_mediana])
            output_file.write(stingbin)
            output_file.close()
            complejidad_media = complejidad(binarios_media) # Calculo la complejidad
            complejidad_mediana = complejidad(binarios_mediana)
            "Guarda los resultados en la string"
            resultados_Complejidad += f"{archivo};{len(binarios_media)};{media};{complejidad_media[1]};{mediana};{complejidad_mediana[1]}\n"
            "Elimina las variables que ya no usamos por cuestiones de espacio"
            printProgressBar(k + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            del(maximos)
            del(binarios_media)
            del(binarios_mediana)


    output_file = open('Resultados3.txt', 'w')
    output_file.write(resultados_Complejidad)
    output_file.close()