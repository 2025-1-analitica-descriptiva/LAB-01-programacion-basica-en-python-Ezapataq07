"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from itertools import groupby


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open("files/input/data.csv", 'r') as file:
        lines = file.readlines()
        sequence = []
        for line in lines:
            columns = line.strip().split('\t')
            key_values = columns[4].strip().split(',')
            sequence.extend((l.split(':')[0], 1) for l in key_values)
    
    result = {}
    for key, group in groupby(sorted(sequence, key=lambda x: x[0]), key=lambda x: x[0]):
        count = sum(value for _, value in group)
        result[key] = count
    return result
