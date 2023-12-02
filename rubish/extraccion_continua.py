import requests

URL:str = 'https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100'

# obtener datos cambiantes del JSON 

def cambios_valenbisi(url: str):
    respuesta = requests.get(url)
    status_code = respuesta.status_code
    datos = respuesta.json()
    if(status_code == 200):
        estaciones_totales:int = datos["total_count"]
        actualizaciones = []
        for i, estacion in enumerate(range(100)):
            actualizacion = []
            clase = datos['results'][i]
            nombre_estacion: str = clase["address"]
            bici_disponibles:int = clase["available"]
            hueco_disponible:int = clase["free"]
            fecha_hora:str = clase["updated_at"]
            actualizacion.append(nombre_estacion)
            actualizacion.append(bici_disponibles)
            actualizacion.append(hueco_disponible)
            actualizacion.append(fecha_hora)
        return(actualizaciones.append(actualizacion))
    else:
        print(f"Error: {status_code}")

print(cambios_valenbisi(URL))