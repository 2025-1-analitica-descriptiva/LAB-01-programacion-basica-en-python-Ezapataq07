"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from itertools import groupby


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", 'r') as file:
        lines = file.readlines()
        sequence = []
        for line in lines:
            columns = line.strip().split('\t')
            key_values = columns[4].split(',')
            sequence.extend((columns[0], int(kv.split(':')[1])) for kv in key_values)
    
    result = {}
    for key, group in groupby(sorted(sequence, key=lambda x: x[0]), key=lambda x: x[0]):
        count = sum(value for _, value in group)
        result[key] = count
    return result