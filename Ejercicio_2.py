import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3, 10, 0, 5]
})
cont = 0


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
            return print(f"Ingreso un productos erroneo, Opciones: {_PRODUCT_DF.product_name.values}")

        return False

    # Busca el stock del producto ingresado
    stock = _PRODUCT_DF.loc[_PRODUCT_DF['product_name']
                            == product_name]['quantity']
    response = True if int(quantity) <= int(stock) else False
    if response == False:
        cont += 1
        if cont > 5:
            return print(f'El stock maximo para el producto {product_name} es {stock.values}.')
    else:
        cont = 0

    return response
