"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from itertools import groupby

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open("files/input/data.csv", 'r') as file:
        lines = file.readlines()
        sequence = []
        for line in lines:
            columns = line.strip().split('\t')
            sequence.append((columns[0], 1))
    
    result = []
    for key, group in groupby(sorted(sequence, key=lambda x: x[0]), key=lambda x: x[0]):
        count = sum(value for _, value in group)
        result.append((key, count))
    return sorted(result, key=lambda x: x[0])