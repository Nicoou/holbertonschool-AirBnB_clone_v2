#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os  # Importa el módulo os para acceder a variables de entorno
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    """ Si estás utilizando DBStorage, agrega la relación con la clase City """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="states")
    else:
        """ Si estás utilizando FileStorage,
        agrega el getter attribute para las ciudades """
        @property
        def cities(self):
            """ Atributo getter que devuelve la lista de instancias de City
            con state_id igual al State.id actual """
            from models import storage
            from models.city import City

            matching_cities = []
            for key in storage.all(City).values():
                if self.id == key.state_id:
                    matching_cities.append(key)
            return matching_cities
