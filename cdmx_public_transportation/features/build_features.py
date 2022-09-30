import os
import pandas as pd
from cdmx_public_transportation.data.make_dataset import data_make_dataset
from cdmx_public_transportation.utils.paths import data_interim

def build_features():
    """
    Generate df_metro.csv and de_metrobus.csv in data/interim ready to model.
    """
    metro, metrobus = data_make_dataset()
    metro = metro.iloc[:,:7]
    metrobus = metrobus.iloc[:,:9]
    metro.to_csv(str(data_interim()) + 'df_metro.csv')
    metrobus.to_csv(str(data_interim()) +  'df_metrobus.csv')
