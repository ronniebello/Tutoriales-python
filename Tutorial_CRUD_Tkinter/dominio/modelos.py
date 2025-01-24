from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class ClienteModel(Base):
    __tablename__ = 'clientes'
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    total = Column(Float)  

    def __repr__(self):
        return f"clientes({self.id}, {self.nombre}, {self.total})"

    def __str__(self):
        return f"clientes({self.id}, {self.nombre}, {self.total})"

class ProductoModel(Base):
    __tablename__ = 'productos'
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey(ClienteModel.id))  # nuevo
    nombre = Column(String)
    precio = Column(Float)
    total = Column(Float) 
    
    cliente = relationship("ClienteModel", foreign_keys="ProductoModel.id_cliente")

    def __repr__(self):
        return f"producto({self.id}, {self.cliente}, {self.nombre}, {self.precio}, {self.total})"

    def __str__(self):
        return f"producto({self.id},  {self.cliente},{self.nombre}, {self.precio}, {self.total})"


