
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
 
from creardb import Base, Experimento, Medicion, Resultado
 

def agregar_medicion(nombre):
    engine = create_engine('sqlite:///labo7.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    experimento = session.query(Experimento).filter(Experimento.nombre == nombre.split('_')).one()
    # nombre, fecha(año,mes,dia), frecuencia (kHz), Vpp(V), ancho(us), tiempo(ms), muestras(Millon), corriente(mA) 
    nueva_medicion = Medicion(nombre=ne[0], experimento = experimento)
    session.add(nuevo_experimento)
    session.commit()

def agregar_resultado(nombre,com_media_t,com_mediana_t,com_media_v,com_mediana_v):
    engine = create_engine('sqlite:///labo7.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    experimento = session.query(Experimento).filter(Experimento.nombre == nombre.split('_')).one()
    # nombre, fecha(año,mes,dia), frecuencia (kHz), Vpp(V), ancho(us), tiempo(ms), muestras(Millon), corriente(mA) 
    nueva_medicion = Medicion(nombre=ne[0], experimento = experimento)
    session.add(nuevo_experimento)
    session.commit()


