import requests
from .mongo import store_data_in_mongodb

# obtener datos basicos del JSON 

def valenbisi_api(url: str):
    respuesta = requests.get(url)
    status_code = respuesta.status_code
    datos = respuesta.json()
    if(status_code == 200):
        estaciones_totales:int = datos["total_count"]
        paradas = []
        for i, estacion in enumerate(range(100)):
            parada=[]
            clase = datos['results'][i]
            nombre_estacion: str = clase["address"]
            numero:int = clase["number"]
            abierta:bool = clase["open"]
            totales:int = clase["total"]
            bici_disponibles:int = clase["available"]
            hueco_disponible:int = clase["free"]
            fecha_hora:str = clase["updated_at"]
            ticket:bool = clase["ticket"]
            coordenadas:list = clase["geo_shape"]["geometry"]["coordinates"]
            parada.append(nombre_estacion)
            parada.append(numero)
            parada.append(abierta)
            parada.append(totales)
            parada.append(bici_disponibles)
            parada.append(hueco_disponible)
            parada.append(ticket)
            parada.append(fecha_hora)
            parada.append(coordenadas)
            primary_key = (f'{numero}_{fecha_hora}')
            store_data_in_mongodb(clase,nombre_estacion,primary_key)
            paradas.append(parada)
        return(paradas)
    else:
        print(f"Error: {status_code}")