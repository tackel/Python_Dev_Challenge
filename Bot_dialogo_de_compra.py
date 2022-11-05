from os import error
import requests
import pandas as pd

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


# Ejercicio 2
cont = 0
_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3, 10, 0, 5]
})


def is_product_available(product_name, quantity):
    """
    Recive: Nombre de producto y cantidad requerida
    Funcion: La funcion verifica si los datos fueron bien ingresados y de ser asi, si existe stock 
            de ese producto
    Retorna: True o False. O un mensaje despues de varios False seguidos
    """
    global cont
    # Compruebo si el producto ingresado existe en la columna product_name
    product_exist = _PRODUCT_DF['product_name'].isin([product_name]).any()
    if product_exist == False:
        cont += 1
        if cont > 5:
            return print('Ingreso mal los datos de forma repetida. El programa se detendra')

        return False

    # Busca el stock del producto ingresado
    stock = _PRODUCT_DF.loc[_PRODUCT_DF['product_name']
                            == product_name]['quantity']
    response = True if int(quantity) <= int(stock) else False
    if response == False:
        cont += 1
        if cont > 5:
            return print('Ingreso mal los datos de forma repetida. El programa se detendra')
    else:
        cont = 0

    return response


# Ejercicio 3
_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
                             "heladoFrozen"]


def validate_discount_code(discount_code):
    """
    Recive: Codigo de descuento enviado por el cliente
    Funcion: La funcion compara el codigo ingresado con los existentes en una lista. Verifica si
            si la diferencia entre estos es mejor a 3
    Retorna: True o False
    """

    # Version que se ajusta al ejemplo
    for code in _AVAILABLE_DISCOUNT_CODES:
        list_code = list(code)
        list_discount_code = list(discount_code)
        if list_code == list_discount_code:
            return True

        diference = set(list_code).symmetric_difference(
            set(list_discount_code))
        if len(diference) < 3:
            return True
    return False

    # Version que considero mas correcta por que tiene en cuenta la cantidad de caracteres repetidos.
    '''
    for code in _AVAILABLE_DISCOUNT_CODES:
        list_code = list(code)
        list_discount_code = list(discount_code)
        if list_code == list_discount_code:
            return True

        list_1 = []
        for i in list_code:
            if i not in list_discount_code:
                list_1.append(i)
            else:
                list_discount_code.remove(i)
        cant = len(list_1 + list_discount_code)
        if cant < 3:
            return True
    return False
    '''


def bot_dialogo():

    print('------------------------------')
    bienvenida_1 = 'Bienvenidos al bot de Heladerías Frozen SRL'
    bienvenida_2 = 'Hoy superamos los 28 grados!!! Bienvenidos a Helados Frozen'
    temp = GeoAPI.is_hot_in_pehuajo()
    print(bienvenida_2 if temp == True else bienvenida_1)

    print('-------------------------------')
    print('Solicite su pedido')
    print('')
    stop = 0
    while True:
        print('Los siguientes son los gustos y stock que tenemos disponibles: ')
        print(_PRODUCT_DF)
        print('')
        product_name = str(input('Ingrese el producto que desea: '))
        quantity = input('Ingrese la cantidad que que desea: ')
        print(f'Usted ha ingresado {quantity} unidades de {product_name}')
        print('')
        hay_stock = is_product_available(product_name, quantity)
        if hay_stock == True:
            print('Ya selecciono su pedido !!!')
            print('')
            break
        elif hay_stock == False:
            print('Ingreso un valor invalido, pruebe nuevamente')
            print('')
        else:
            stop = 1
            break

    while stop == 0:

        discount_code = input(
            'Ingrese su codigo de descuento. Si no tiene uno ingrese: EXIT: ')
        if discount_code == 'EXIT':
            print('------- Eligio no ingresar un codigo de descuento -------')
            break
        codigo = validate_discount_code(discount_code)
        if codigo == True:
            print('------- Ingreso un codigo de forma correcta -------')
            break
        elif codigo == False:
            print('')
            print('------- Ingreso un codigo erroneo -------')
            opcion = input('Quiere volver a intentarlo? Ingrese: si o no: ')
            if opcion == 'si':
                pass
            else:
                print('')
                print('Usted no ingresara codigo de descuento.')
                break
    if stop == 0:
        print('')
        print('---------------------------------------------')
        print('Su pedido ha sido confirmado. Muchas gracias.')
        print('---------------------------------------------')
    else:
        print('')
        print('---------------------------------------------')
        print('Pedido Cancelado')
        print('---------------------------------------------')


if __name__ == "__main__":
    bot_dialogo()
