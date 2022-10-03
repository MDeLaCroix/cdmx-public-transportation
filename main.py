from app import *
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

def run():
    title()
    first_paragraph()
    fig = deploy_model()
    st.pyplot(fig, clear_figure= False)
    #st.title('Energía eléctrica necesaria para el funcionamiento del STC Metro de la Ciudad de México')

if __name__ == '__main__':
    run()
    #generate df_metro and df_metrobus in folder data/interim

