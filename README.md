# cdmx-public-transportation

## Introducción

El siguiente análisis pretende mostrar el uso de la ciencia de datos para determinar el consumo de energía eléctrica del STC Metro de la Ciudad de México. Para hacer este análisis obtenida del Instituto Nacional de Estadística y Geografía (INEGI) en su apartado «Economía y Sectores Productivos» en la opción «Transporte/Transporte de Pasajeros». La información ha sido extraída el 27 de septiembre de 2022 del siguiente [enlace](https://www.inegi.org.mx/app/tabulados/?nc=100100042&idrt=181&opc=t).

## Instrucciones de uso

Haz un clone de este repositorio con el código

```
$ git clone https://github.com/MDeLaCroix/cdmx-public-transportation.git
```

## Creación de ambiente

Para proceder en este paso es necesario tener `conda` (opcionalmente `mamba`).

```
conda env create -f environment.yml
activate cdmx-pt
```

o

```
mamba env create -f environment.yml
activate cdmx-pt
```

## Inicar aplicación

Una vez dentro de la carpeta de la aplicación deberá usarse el siguiente código:

```
streamlit run main.py
```

Si este código no funcionara es necesario indicar que `streamlit` es un módulo de `python`.

- En Linux o MacOs:
```
python -m streamlit main.py
```

- En Windows:
```
py -m streamlit main.py
```



## Estructura del proyecto

```
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   └── raw            <- Files as they were downloaded from the source web page.
    │
    ├── models             <- Contains the model and temporarily its display.
    │
    ├── notebooks          <- It is the complete model in a single file to be able to be analyzed 
    │                         without modules, the use of Spyder is recommended. It will include 
    │                         a Jupyter Notebook.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    └── cdmx_public_transportation     <- Source code for use in this project.
        ├── __init__.py                 <- Makes cdmx_public_transportation a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to use in models.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py
```



## El proyecto en el futuro

Se incorporará análisis de otros sistemas de transporte de la Ciudad de México, en la cuál se pretende usar otros modelos de ciencia de datos. Una condición para incorporarse a este modelo es que los datos estudiados deben ser reales y deben ser obtenidos de instancias gubernamentales como el **INEGI** ([www.inegi.org.mx](https://www.inegi.org.mx/)) o el sitio de **datos abiertos de la Ciudad de México** ([datos.cdmx.gob.mx](datos.cdmx.gob.mx)).