import sqlalchemy as db
from sqlalchemy.orm import Session
from dominio.modelos import ProductoModel
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


class ServicioProducto():

    def __init__(self):
        # Creamos el motor de la base de datos
        self.engine = db.create_engine(
            "sqlite:///db/tienda.db", echo=True, future=True)

    # Metodo para registrar un producto -------------------------
    def register(self, nombre, precio):
        product = ProductoModel()
        product.nombre = nombre
        product.precio = precio

        with Session(self.engine) as session:
            session.add(product)
            session.commit()

    # Metodo para modificar un producto -------------------------
    def modificar(self, nombre, precio, producto_id):
        try:
            # Buscamos el producto con el ID proporcionado
            with Session(self.engine) as session:
                product = session.query(ProductoModel).filter(
                    ProductoModel.id == producto_id).one()

                # Modificamos los valores del producto encontrado
                product.nombre = nombre
                product.precio = precio

                # Grabamos los coambios en la base de datos
                session.commit()
                print(f"El productocon el ID {
                      producto_id}. Fue cambiado exitosamente")

        except NoResultFound:
            print(f"No se encontro ningun el productocon el ID {
                  producto_id}. No se realizo ningun cambio")
            return False

        except Exception as e:
            print(f"Error al modificar el producto con ID {producto_id}: {e}")
            return False

    # Metodo para consultar un producto -------------------------
    def obtener_productos(self) -> List[ProductoModel]:
        productos: ProductoModel = None
        with Session(self.engine) as session:
            productos= session.query(ProductoModel).all()
        return productos

    # Metodo para eliminar un producto -------------------------
    def eliminar(self, producto_id):
        # Buscamos el producto con el ID proporcionado
        with Session(self.engine) as session:
            product = session.query(ProductoModel).filter_by(id = producto_id).first()
            if product:
                try:
                    # Eliminamos el producto encontrado
                    session.delete(product)
                    # Grabamos los coambios en la base de datos
                    session.commit()
                    print(f"El productocon el ID {producto_id}. Fue eliminado exitosamente")
                
                except IntegrityError as e:
                    session.rollback()
                    print(f"Error al eliminar el producto con ID {producto_id}: Error: {e}")
            else:
                print(f"No se encontro ningun el productocon el ID {producto_id}. No se elimino ningun producto")
                return False        

                

        
