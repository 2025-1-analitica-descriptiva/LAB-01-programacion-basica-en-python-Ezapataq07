"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from itertools import groupby


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    with open("files/input/data.csv", 'r') as file:
        lines = file.readlines()
        sequence = []
        for line in lines:
            columns = line.strip().split('\t')
            sequence.append((int(columns[1]), columns[0]))
    
    result = []
    for key, group in groupby(sorted(sequence, key=lambda x: x[0]), key=lambda x: x[0]):
        values = list(set(value for _, value in group))
        result.append((key, sorted(values, key=lambda x: x[0])))
    return sorted(result, key=lambda x: x[0])