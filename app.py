import matplotlib.pyplot as plt
import app as st
import streamlit as st
from models.model import Model

def title():
    st.title('Energía eléctrica necesaria para el funcionamiento del STC Metro de la Ciudad de México')

def first_paragraph():
    st.markdown("""
    ## Introducción
    El siguiente análisis pretende mostrar el uso de la ciencia de datos para determinar el consumo de energía \
    eléctrica del STC Metro de la Ciudad de México. Para hacer este análisis se ha considerado información \
    obtenida del Instituto Nacional de Estadística y Geografía (INEGI) en su apartado «Economía y Sectores \
    Productivos» en la opción «Transporte/Transporte de Pasajeros». La información ha sido extraída el 27 de \
    septiembre de 2022 del siguiente [enlace](https://www.inegi.org.mx/app/tabulados/?nc=100100042&idrt=181&opc=t)\
    """)

def target_paragraph():
    st.markdown("""
    ## Objetivo del análisis
    Este análisis tiene como objetivo determinar el consumo de energía eléctrica en el servicio del STC Metro \
    de la Ciudad de México, de esta manera es más fácil determinar los costos que pueden generarse de modificar \
    el servicio o incrementar la cantidad de pasajeros.
    En la actualidad hemos visto esto representado en corredores (líneas de Metro) que han visto modificado ya \
    sea por mantenimiento o por incidentes, así como el aumento o disminución del número de usuario de este \
    sistema ya sea por la implementación de otros sistemas de transporte o consecuencia de factores que \
    impactan a la Ciudad de México (ejemplo, la pandemia por COVID-19).
    """)

def analysis_paragraph():
    st.markdown("""
    ## Análisis de la información
    Los datos obtenidos cuentan con siete elementos:
    1. **Año**, año en el que se obtuvo el registro.
    2. **Mes**, mes en el que se obtuvo el registro.
    3. **Longitud en servicio (km)**, cuántos kilómetros estuvieron habilitados para el servicio a psajeros.
    4. **Trenes en servicio**, cuántos trenes estuvieron en servicio en el año-mes descrito.
    5. **Kilómetros recorridos (Miles de kilómetros)**, cuántos kilómetros recorrieron los trenes en año-mes \
    descrito, esta cantidad está descrita en miles de kilómetros.
    6. **Pasajeros transportados (Millones de pasajeros)**, cantidad de personas transportadas en el año-mes, \
    representada en millones de pasajeros.
    7. **Energía eléctrica consumida (Miles de KWH)**, es la cantidad de energía eléctrica consumida en el \
    año-mes descrita en miles de kilowatt horas.
    Por la naturaleza del análisis los dos primeros datos no son considerados dentro del modelo. Es por ello \
    que los **puntos 3, 4, 5, 6 y 7** han sido sometidos a análisis.
    El objetivo de ese estudio es **determinar los kilowatt horas**, en otras palabras nuestra variable objetivo \
    es el **punto 7**, esto es el consumo de energía eléctrica dependiendo de las variables
    Se determinó que los **puntos 4 y 5**, tienen un alto nivel de **multicolinealidad**, a través del método \
    de **factores variables de inflación (VIF)**, esto es, que existe una alta relación entre estas variables \
    y el resto de los datos independientes, por esta razón, se ha decidido eliminar estos factores ya que \
    dejarlos generará un sobreajuste de datos.
    """)

def how_to_paragraph():
    st.markdown("""
    ## Cómo usar esta aplicación
    Cambie los valores de los controles deslizantes «**Longitud del servicio (kilómetros)**» y «**Pasajeros \
    transportados (Millones de pasajeros)**», una vez que estos están en la posición deseada de clic en el \
    botón «**Calcular**», esto mostrará una gráfica la cual mostrará los siguientes elementos:
    - **Pasajeros transportados (Millones de pasajeros)**, en el eje X.
    - **Energía eléctrica consumida (Miles de KWH)**, en el eje Y.
    - **Longitud del servicio (kilómetros)**, mostrada por el color de cada punto observado, mientras más \
    oscuro el color mayo longitud de servicio, auxiliase de la barra de color para encontrar el valor.
    - **Proyección del consumo de energía eléctrica**, mostrada en una línea roja continua ascendente, detalla \
    la evolución del consumo dependiendo de la cantidad de pasajeros. La inclinación de esta línea variará \
    dependiendo de lo seleccionado en el control deslizante «Longitud del servicio (kilómetros)».
    - **Consumo de energía eléctrica**, mostrada en una línea intermitente horizontal.
    """)

def request_km():
    km = st.slider(label= 'Longitud del servicio (kilómetros)',
        min_value=0,
        max_value=500,
        value= 200,
        step= 10
        )
    return km

def request_px():
    px = st.slider(label= 'Pasajeros transportados (Millones de pasajeros)',
        min_value=0,
        max_value=300,
        value=80,
        step= 10
        )
    return px

def deploy_model():
    km = request_km()
    px = request_px()
    if st.button('Calcular'):
        model = Model(km, px)
        fig = model.figure
        prediction = model.y_hat
    else:
        fig = plt.figure()
        prediction = ""
    return fig, prediction

