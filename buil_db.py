import sqlalchemy as db # Importamos sqlalchemy para trabajar con la base de datos
import dominio.modelos as modelos # Importamos los modelos de la base de datos
import util.generico as gen # Importamos la funcion para crear carpetas

#Nombre de la carpeya donde queremos crear la base de datos
nombre_carpeta = "db"

# La ruta donde se creara la carpeta para almasenar la base de datos
ruta ="./"

# Creamos la carpeta si no existe
gen.crear_carpeta_si_no_existe(ruta, nombre_carpeta)
engine=db.create_engine("sqlite:///"+ruta+nombre_carpeta+"/tienda.db", echo=True, future=True) # Creamos el motor de la base de datos

modelos.Base.metadata.create_all(engine) # Creamos las tablas en la base de datos