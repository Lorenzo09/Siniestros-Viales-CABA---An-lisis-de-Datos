import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def verificar_tipo_datos(df):
    '''
    Realiza un análisis de los tipos de datos y la presencia de valores nulos en un DataFrame.

    Esta función toma un DataFrame como entrada y devuelve un resumen que incluye información sobre
    los tipos de datos en cada columna, el porcentaje de valores no nulos y nulos, así como la
    cantidad de valores nulos por columna.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        pandas.DataFrame: Un DataFrame que contiene el resumen de cada columna, incluyendo:
        - 'nombre_campo': Nombre de cada columna.
        - 'tipo_datos': Tipos de datos únicos presentes en cada columna.
        - 'no_nulos_%': Porcentaje de valores no nulos en cada columna.
        - 'nulos_%': Porcentaje de valores nulos en cada columna.
        - 'nulos': Cantidad de valores nulos en cada columna.
    '''

    mi_dict = {"nombre_campo": [], "tipo_datos": [], "no_nulos_%": [], "nulos_%": [], "nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        mi_dict["nombre_campo"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
        mi_dict["no_nulos_%"].append(round(porcentaje_no_nulos, 2))
        mi_dict["nulos_%"].append(round(100-porcentaje_no_nulos, 2))
        mi_dict["nulos"].append(df[columna].isnull().sum())

    df_info = pd.DataFrame(mi_dict)
        
    return df_info

def verifica_duplicados_por_columna(df, columna):
    '''
    Verifica y muestra filas duplicadas en un DataFrame basado en una columna específica.

    Esta función toma como entrada un DataFrame y el nombre de una columna específica.
    Luego, identifica las filas duplicadas basadas en el contenido de la columna especificada,
    las filtra y las ordena para una comparación más sencilla.

    Parameters:
        df (pandas.DataFrame): El DataFrame en el que se buscarán filas duplicadas.
        columna (str): El nombre de la columna basada en la cual se verificarán las duplicaciones.

    Returns:
        pandas.DataFrame or str: Un DataFrame que contiene las filas duplicadas filtradas y ordenadas,
        listas para su inspección y comparación, o el mensaje "No hay duplicados" si no se encuentran duplicados.
    '''
    # Se filtran las filas duplicadas
    duplicated_rows = df[df.duplicated(subset=columna, keep=False)]
    if duplicated_rows.empty:
        return "No hay duplicados"
    
    # se ordenan las filas duplicadas para comparar entre sí
    duplicated_rows_sorted = duplicated_rows.sort_values(by=columna)
    return duplicated_rows_sorted