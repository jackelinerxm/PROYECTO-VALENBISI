import requests

URL:str = 'https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100'

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
            bici_disponibles:list = []
            hueco_disponible:list = []
            ticket:bool = clase["ticket"]
            fecha_hora:list = []
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
            paradas.append(parada)
        return(paradas)
    else:
        print(f"Error: {status_code}")
    
valenbisi_api(URL)

