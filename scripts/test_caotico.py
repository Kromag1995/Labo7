import os
import numpy as np
import matplotlib.pyplot as plt
from .falsos_vecinos import test_fv 
from .lyapunov import lyapunov

class bcolors:
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    OKBLUE = '\033[94m'
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_caotico():
    """
    Script para calcular la dimension de embedding utilizando primeros vecinos y
    luego calcular los exponentes de lyapunov para determinar la caoticidad del sistema
    """
    input_path = './maximos/Nobinarizados/'
    output_path = './falsos vecinos/'
    if 'falsos vecinos' not in os.listdir():
        os.mkdir(output_path)
    paso = False
    for dirpath,dirname, files in os.walk(input_path):
        for archivo in files:

            datos = np.genfromtxt(dirpath+'/'+archivo, dtype= None)
            
            print(f"{bcolors.OKBLUE}{archivo}{bcolors.ENDC}")
            
            fv, caotico, neecsito_ver_mas, d_E, saltar  =  test_fv(datos, 1, 20)
            
            if saltar:
                continue
            
            print(fv)
            np.savetxt(output_path+archivo+"fv", np.append(d_E, fv) , delimiter=',', header="La primera linea es la dimension de embedding, sigue la matriz de false_nearest")
            
            lyap = 0
            paso =False
            if caotico and d_E >1:
                print(f"Dimension de embeding : {d_E}" )
                lyap,paso = lyapunov(datos, d_E)
                if paso:
                    print("Es Caotico")
                else:
                    print("No es caotico")
                if len(lyap)>0:
                    np.savetxt(output_path+archivo+"lyap", lyap, delimiter=',') 
            else:
                print("No es caotico")
                print("Proporcion de falsos vecinos : " + str(fv[d_E-1,1]))
