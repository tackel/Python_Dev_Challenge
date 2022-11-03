
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


validate_discount_code('primavera202122')
