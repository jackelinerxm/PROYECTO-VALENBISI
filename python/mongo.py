import pymongo
from datetime import datetime
import time

def connect_to_mongodb():
    # Conéctate a tu instancia de MongoDB (asegúrate de tener MongoDB ejecutándose localmente o especifica la URL de conexión)
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Selecciona la base de datos y la colección
    db = client["mi_base_de_datos"]
    collection = db["mi_coleccion"]

    return collection

def store_data_in_mongodb(data):
    # Conecta a MongoDB
    collection = connect_to_mongodb()

    # Crea un documento con datos y una marca de tiempo
    document = {
        "data": data,
        "timestamp": datetime.now()
    }

    # Inserta el documento en la colección
    collection.insert_one(document)

if __name__ == "__main__":
    while True:
        # Datos que deseas almacenar en MongoDB
        data_to_store = "Hola, MongoDB!"

        # Llama a la función para almacenar datos en MongoDB
        store_data_in_mongodb(data_to_store)

        # Espera 5 minutos antes de almacenar el siguiente conjunto de datos
        time.sleep(300)  # 300 segundos = 5 minutos
