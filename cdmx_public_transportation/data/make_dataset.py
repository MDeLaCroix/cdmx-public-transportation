import pandas as pd
from cdmx_public_transportation.utils.paths import data_raw_dir

def data_make_dataset():
    """Generate dataset from file 'Metro.csv' and 'Metrobus.csv' in file data/raw.

    It's necessary to define:
    metro, metrobus = make_dataset()

    Returns:
        pandas.dataset: variabes named 'metro' and 'metrobus'.
    """
    DATA_DIR = data_raw_dir()
    metro = pd.read_csv(str(DATA_DIR) + 'Metro.csv')
    metrobus = pd.read_csv(str(DATA_DIR) + 'Metrobus.csv')
    return metro, metrobus