from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
 
from creardb import Experimento, Base, Medicion, Resultado
 
engine = create_engine('sqlite:///labo7.db')


Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()
 # nombre, fecha(año,mes,dia), frecuencia (kHz), Vpp(V), ancho(us), tiempo(ms), muestras(Millon), corriente(mA) 
"""
ne = ["20210407-0001", date(2021,4,7), "180", "4", "3.5", "500", "39", "1896"]
nuevo_experimento = Experimento(nombre=ne[0], fecha = ne[1], frecuencia = ne[2], voltaje = ne[3],
    ancho=ne[4], tiempo=ne[5], muestras=ne[6], corriente= ne[7])
session.add(nuevo_experimento)
ne = ["20210407-0001", date(2021,4,7), "180", "4", "3.5", "500", "39", "1850"]
nuevo_experimento = Experimento(nombre=ne[0], fecha = ne[1], frecuencia = ne[2], voltaje = ne[3],
    ancho=ne[4], tiempo=ne[5], muestras=ne[6], corriente= ne[7])
session.add(nuevo_experimento)
ne = ["20210407-0001", date(2021,4,7), "180", "4", "3.5", "500", "39", "1800"]
nuevo_experimento = Experimento(nombre=ne[0], fecha = ne[1], frecuencia = ne[2], voltaje = ne[3],
    ancho=ne[4], tiempo=ne[5], muestras=ne[6], corriente= ne[7])
session.add(nuevo_experimento)
ne = ["20210407-0001", date(2021,4,7), "180", "4", "3.5", "500", "39", "1750"]
nuevo_experimento = Experimento(nombre=ne[0], fecha = ne[1], frecuencia = ne[2], voltaje = ne[3],
    ancho=ne[4], tiempo=ne[5], muestras=ne[6], corriente= ne[7])
session.add(nuevo_experimento)
ne = ["20210407-0001", date(2021,4,7), "180", "4", "3.5", "500", "39", "1700"]
nuevo_experimento = Experimento(nombre=ne[0], fecha = ne[1], frecuencia = ne[2], voltaje = ne[3],
    ancho=ne[4], tiempo=ne[5], muestras=ne[6], corriente= ne[7])
session.add(nuevo_experimento)
ne = ["20210407-0001", date(2021,4,7), "180", "4", "3.5", "500", "39", "1950"]
nuevo_experimento = Experimento(nombre=ne[0], fecha = ne[1], frecuencia = ne[2], voltaje = ne[3],
    ancho=ne[4], tiempo=ne[5], muestras=ne[6], corriente= ne[7])
session.add(nuevo_experimento)
ne = ["20210407-0001", date(2021,4,7), "180", "4", "3.5", "500", "39", "2000"]
nuevo_experimento = Experimento(nombre=ne[0], fecha = ne[1], frecuencia = ne[2], voltaje = ne[3],
    ancho=ne[4], tiempo=ne[5], muestras=ne[6], corriente= ne[7])
session.add(nuevo_experimento)
"""
session.commit()
