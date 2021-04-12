import numpy as np
from scipy.signal import find_peaks
import os
from .utils import printProgressBar

def detectar_maximos(mode):
    if not  "maximos" in os.listdir():
        os.mkdir("maximos")
        os.mkdir("maximos/Nobinarizados")
        os.mkdir("maximos/Binarizados")
    datos=[]
    Qd = len(os.listdir('./datos'))
    Qdd = 0
    l = 10
    printProgressBar(0, l*Qd, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for dirpath,dirname, files in os.walk('./datos'):
        for i, archivo in enumerate(files):
            if (mode in archivo):

                tiempos,tira = np.loadtxt(dirpath+'/'+archivo,skiprows=3, delimiter=",", unpack=True)

                inf = tira != np.inf
                count_inf = np.sum(tira == np.inf)
                slices = tira[inf] > 0.001
                
                filtrado_V = tira[slices]
                filtrado_t = tiempos[slices]

                peaks, _ = find_peaks(filtrado_V,distance = 15, height=0.05)
                maximos_V = filtrado_V[peaks]
                maximos_t = filtrado_t[peaks]

                #print(f'La cantidad de picos saturados es {count_inf} de {len(filtrado_V)}')
                #print(f'Esto representa %{count_inf*100/len(filtrado_V)}')
                #print(f'La cantidad de picos saturados es {count_inf} de {len(maximos_V)}')
                #print(f'Esto representa %{count_inf*100/len(maximos_V)}')
                archivo = archivo.replace(".csv","").replace("DATA_","").replace("Millones","")
                np.savetxt(f"./maximos/Nobinarizados/{archivo}_V",maximos_V)
                np.savetxt(f"./maximos/Nobinarizados/{archivo}_t",maximos_t)
                printProgressBar(i + 1 + l*Qdd, l*Qd, prefix = 'Progress:', suffix = 'Complete', length = 50)
                del(tira)
                del(filtrado_t)
                del(filtrado_V)
                del(maximos_t)
                del(maximos_V)
                del(peaks)
                del(tiempos)
        Qdd += 1