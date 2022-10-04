from app import *
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

def run():
    title()
    first_paragraph()
    target_paragraph()
    analysis_paragraph()
    how_to_paragraph()
    fig, prediction = deploy_model()
    pred_text = f'Dados los parámetros proporcionados el consumo será de {prediction} KWH,'
    st.text(pred_text)
    st.pyplot(fig, clear_figure= False)


if __name__ == '__main__':
    run()
    #generate df_metro and df_metrobus in folder data/interim

