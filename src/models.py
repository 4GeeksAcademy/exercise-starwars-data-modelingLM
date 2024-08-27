import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
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

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id
        }


class FavoritoPersonaje(Base):
    __tablename__ = 'favorito_personaje'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    
    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
