import pandas as pd
import numpy as np
import os


def conjunto_itinerarios(name):
    
    df_json1 = pd.read_json(fr'../data_raw/conjunto_itinerarios/{name}' , lines=True)
    df1 = pd.json_normalize(df_json1._id)
    df_json1['_id'] =df1['$oid']
    return df_json1


def conjunto_estaticos(name):
    
    df_json = pd.read_json(fr'../data_raw/conjunto_estaticos/{name}', lines=True)
    df_json = df_json.explode('stations').reset_index()
    df = pd.json_normalize(df_json.stations)
    df.insert(0,'_id','')
    df['_id'] = df_json['_id']
    return df



def agrupa_data(direct, funcion):

    with os.scandir(direct) as ficheros:

        for count, fichero in enumerate(ficheros):
            nombre = fichero.name
            if count == 0:
                data = funcion(nombre)

            else:
                data2 = funcion(nombre)
                data = pd.concat([data, data2])
                
    return data



def check_nan(df: pd.DataFrame) -> None:
    
    nan_cols=df.isna().mean() * 100  # el porcentaje
    
    display(f'N nan cols: {len(nan_cols[nan_cols>0])}')
    display(nan_cols[nan_cols>0])
    
    plt.figure(figsize=(10, 6))  # inicia la figura y establece tamaño

    sns.heatmap(df.isna(),  # mapa de calor
                yticklabels=False,
                cmap='viridis',
                cbar=False)

    plt.show();