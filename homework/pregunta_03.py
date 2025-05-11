"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from itertools import groupby

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open("files/input/data.csv", 'r') as file:
        lines = file.readlines()
        sequence = []
        for line in lines:
            columns = line.strip().split('\t')
            sequence.append((columns[0], int(columns[1])))
    
    result = []
    for key, group in groupby(sorted(sequence, key=lambda x: x[0]), key=lambda x: x[0]):
        count = sum(value for _, value in group)
        result.append((key, count))
    return sorted(result, key=lambda x: x[0])