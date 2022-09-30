import os

CURRENT_DIR = os.getcwd()

def data_raw_dir():
    """Generate path to data/raw/

    Returns:
        path to data/raw/
    """
    DATA_RAW_DIR = os.path.join(CURRENT_DIR, 'data', 'raw' + os.sep)
    return DATA_RAW_DIR

def data_make_dataset():
    """Generate path to cdmx-public-transportation/data/

    Returns:
        path to dmx-public-transportation/data/
    """
    MAKE_DATASET_DIR = os.path.join(CURRENT_DIR, 'cdmx-public-transportation', 'data' + os.sep)
    return MAKE_DATASET_DIR

def data_interim():
    """Generate path to data/interim/

    Returns:
        path to data/interim/
    """
    INTERIM_DIR = os.path.join(CURRENT_DIR, 'data', 'interim' + os.sep)
    return INTERIM_DIR

