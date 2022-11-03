from os import error
import requests

# Ejercicio 1


class GeoAPI:

    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    API = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric'

    @classmethod
    def is_hot_in_pehuajo(cls):
        """ Retorna True si la temperatura es mayor a 28 ° celcius  """
        try:
            data = requests.get(cls.API, timeout=10)
            if data.status_code == 200:
                return True if data.json()['main']['temp'] > 28 else False
            return False
        except error as e:
            print(e)


GeoAPI.is_hot_in_pehuajo()
