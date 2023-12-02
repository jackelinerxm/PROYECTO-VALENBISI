import requests

URL:str = 'https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100'

# obtener datos basicos del JSON 

def valenbisi_api(url: str):
    respuesta = requests.get(url)
    status_code = respuesta.status_code
    datos = respuesta.json()
    if(status_code == 200):
        estaciones_totales:int = datos["total_count"]
        for i, estacion in enumerate(range(100)):
            clase = datos['results'][i]
            nombre_estacion: str = clase["address"]
            numero:int = clase["number"]
            abierta:bool = clase["open"]
            totales:int = clase["total"]
            bici_disponibles:int = clase["available"]
            hueco_disponible:int = clase["free"]
            ticket:bool = clase["ticket"]
            fecha_hora:str = clase["updated_at"]
            coordenadas:list = clase["geo_shape"]["geometry"]["coordinates"]
    else:
        print(f"Error: {status_code}")

valenbisi_api(URL)

