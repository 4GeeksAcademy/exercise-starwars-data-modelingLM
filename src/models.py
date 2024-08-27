import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    favoritos_planetas = relationship('FavoritoPlaneta', backref='usuario')
    favoritos_personajes = relationship('FavoritoPersonaje', backref='usuario')

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    favoritos_planetas = relationship('FavoritoPlaneta', backref='planeta')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eyes_color = Column(String(250), nullable=False)
    favoritos_personajes = relationship('FavoritoPersonaje', backref='personaje')

class FavoritoPlaneta(Base):
    __tablename__ = 'favorito_planeta'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    usuario = relationship('Usuario', backref='favoritos_planetas')
    planeta = relationship('Planeta', backref='favoritos_planetas')


class FavoritoPersonaje(Base):
    __tablename__ = 'favorito_personaje'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    usuario = relationship('Usuario', backref='favoritos_personajes')
    personaje = relationship('Personaje', backref='favoritos_personajes')



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
