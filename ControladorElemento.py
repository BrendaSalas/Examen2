import requests
from Elemento import Elemento  # Asegúrate de que la clase Elemento esté definida en un archivo llamado elemento.py

class ControladorElemento:
    def __init__(self, url):
        self.url = url

    '''def obtener_elementos(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            data = response.json()
            print(data)  # Agrega esta línea para ver la respuesta de la API
            elementos = [
                Elemento(item["id"], item["element"], item["group"], item["periodo"])
                for item in data
            ]
            return elementos
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos: {e}")  # O manejar el error de otra manera
            return []'''
    def obtener_elementos(self):
        try:
            # Limitar la solicitud a 100 elementos
            response = requests.get(f"{self.url}?limit=100")
            response.raise_for_status()
            data = response.json()
            # Convertir los datos en una lista de objetos Elemento
            elementos = [
                Elemento(item["id"], item["element"], item.get("group", ""), item.get("periodo", ""))
                for item in data
            ]
            return elementos
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos: {e}")
            return []