import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3, 10, 0, 5]
})
cont = 0


def is_product_available(product_name, quantity):
    global cont
    # Compruebo si el producto ingresado existe en la columna product_name
    product_exist = _PRODUCT_DF['product_name'].isin([product_name]).any()
    if product_exist == False:
        cont += 1
        if cont > 5:
            return print('Ha ingresado valores incorrectos muchas veces.')
        return False

    # Busca el stock del producto ingresado
    stock = _PRODUCT_DF.loc[_PRODUCT_DF['product_name']
                            == product_name]['quantity']
    response = True if int(quantity) <= int(stock) else False
    if response == False:
        cont += 1
    else:
        cont = 0
    if cont > 5:
        return print('Ha ingresado valores incorrectos muchas veces.')
    return response


# ejemplos de pedidos
print(is_product_available('Granizad', 2))
print(is_product_available('Granizad', 2))
print(is_product_available('Granizad', 2))
print(is_product_available('Granizad', 2))
print(is_product_available('Granizad', 2))
print(is_product_available('Granizad', 2))
print(is_product_available('Granizad', 2))
print(is_product_available('Granizado', 2))
print(is_product_available('Granizad', 2))
print(is_product_available('Granizad', 2))
print(is_product_available('Granizad', 2))
