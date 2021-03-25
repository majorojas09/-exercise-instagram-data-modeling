import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Login(Base):
    __tablename__ = 'login'
    username = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)

class Register(Base):
    __tablename__ = 'userRegister'
    userId = Column(Integer, primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    username_User = Column(String(250), ForeignKey('login.username'))
    password_User = Column(String(250), nullable=False)
    login = relationship(Login)
    
class Planets(Base):
    __tablename__ = 'planets'
    planetId = Column(Integer, primary_key=True)
    planetName = Column(String(250), nullable=False)
    planetDescription = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    orbitalPeriod = Column(String(250), nullable=False)
    rotationPeriod = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    characterId = Column(Integer, primary_key=True)
    characterName = Column(String(250), nullable=False)
    characterDescription = Column(String(250), nullable=False)
    birthYear = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    skinColor = Column(String(250), nullable=False)
    eyeColor = Column(String(250), nullable=False)

class FavoritePlanet(Base):
    __tablename__ = 'favoritePlanet'
    favoriteId_Planet = Column(Integer, primary_key=True)
    planetId_Planet = Column(Integer,  ForeignKey('planets.planetId'))
    userId_User = Column(Integer,  ForeignKey('userRegister.userId'))
    userRegister = relationship(Register)
    planets = relationship(Planets)

class FavoriteCharacter(Base):
    __tablename__ = 'favoriteCharacter'
    favoriteId_Character = Column(Integer, primary_key=True)
    characterId_Character = Column(Integer,  ForeignKey('characters.characterId'))
    IdUser_User = Column(Integer,  ForeignKey('userRegister.userId'))
    userRegister = relationship(Register)
    characters = relationship(Characters)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')