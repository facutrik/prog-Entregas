def validar_texto(texto, campo):

    if texto.strip() == "":
        raise ValueError(f"El campo {campo} no puede estar vacío")

    if not texto.replace(" ", "").isalpha():
        raise ValueError(f"El campo {campo} solo debe contener letras")

    return texto


def validar_numero(numero, campo):

    if numero.strip() == "":
        raise ValueError(f"El campo {campo} no puede estar vacío")

    if not numero.isdigit():
        raise ValueError(f"El campo {campo} solo debe contener números")

    return numero
