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