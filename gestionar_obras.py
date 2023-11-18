from abc import ABC
import pandas as pd
from peewee import *
import sqlite3
from modelo_orm import *

class GestionarObra(ABC):
    nombre_archivo = "datos.csv"
    df = None
    conexion = None
    
    @classmethod
    def extraer_datos(cls):
        try:
            cls.df = pd.read_csv(cls.nombre_archivo)
            return cls.df
        except FileNotFoundError as e:
            print(f"Error: El archivo no se encontro. {e}")
            return None
        except pd.errors.EmptyDataError as e:
            print(f"Error: El archivo esta vacio. {e}")
            return None



    @classmethod
    def conectar_db(cls):
        try:
            cls.conexion = sqlite3.connect("obras_urbanas.db")
            print("Base de datos abierta")
            return cls.conexion
        except sqlite3.DatabaseError as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        
        
        
    @classmethod    
    def mapear_orm(cls):  
     try:
        sqlite_db.create_tables([EntornoF, ObrasPublicas], safe=True)
        print("Se mapearon las tablas y las columnas")
        return sqlite_db
     except sqlite3.DataError as e:
         print(f"Error al conectar la base de datos: {e}")
         return None
         
        
    @classmethod
    def limpiar_datos(cls):
        pass
    @classmethod
    def cargar_datos(cls):
        pass
    @classmethod
    def nueva_obra(cls):
        pass
    @classmethod
    def obtener_indicadores(cls):
        pass


# Ejemplo de uso
gestor_obra = GestionarObra()
datos_extraidos = gestor_obra.extraer_datos()
conectarBD= gestor_obra.conectar_db()
mapear = gestor_obra.mapear_orm()






