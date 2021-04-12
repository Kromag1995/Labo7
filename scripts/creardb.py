import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Experimento(Base):
    __tablename__ = "Experimento"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(250), nullable=False)
    fecha = Column(Date)
    frecuencia = Column(Float)
    voltaje = Column(Float)
    ancho =  Column(Float)
    tiempo = Column(Float)
    muestras = Column(Float)
    corriente = Column(Float)

class Medicion(Base):
    __tablename__ = "Medicion"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(250), nullable=False)
    experimento_id = Column(Integer, ForeignKey('Experimento.id'))
    experimento = relationship(Experimento)

class Resultado(Base):
    __tablename__ = "Resultado"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(250), nullable=False)
    complejidad_media_t = Column(Float)
    complejidad_mediana_t =  Column(Float)
    complejidad_media_v = Column(Float)
    complejidad_mediana_v =  Column(Float)
    medicion_id = Column(Integer, ForeignKey('Medicion.id'))
    medicion = relationship(Medicion)

engine = create_engine('sqlite:///labo7.db')

Base.metadata.create_all(engine) 