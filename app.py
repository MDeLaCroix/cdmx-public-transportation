import matplotlib.pyplot as plt
import app as st
import streamlit as st
from models.model import Model

def title():
    st.title('Energía eléctrica necesaria para el funcionamiento del STC Metro de la Ciudad de México')

def first_paragraph():
    st.markdown("""
    ## Introducción
    El siguiente anáisis pretende mostrar el uso de la ciencia de datos para determinar el consumo de energía \
    electrica del STC Metro de la Ciudad de México. Para hacer este análisis se ha considerado información \
    obtenida del Instituto Nacional de Estadística y Geografía (INEGI) en su apartado «Econonomía y Sectores \
    Productivos» en la opción «Transporte/Transporte de Pasajeros». La infrmación ha sido extraída el 27 de \
    septiembre de 2022 del siguiente [enlace](https://www.inegi.org.mx/app/tabulados/?nc=100100042&idrt=181&opc=t)\
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
        model.figure
        plt.show()

