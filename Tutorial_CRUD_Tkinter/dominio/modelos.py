from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class ProductoModel(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    precio = Column(Float)

    def __repr__(self):
        return f"producto({self.id}, {self.nombre}, {self.precio})"

    
    def __str__(self):
        return f"producto({self.id}, {self.nombre}, {self.precio})"
