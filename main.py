import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from utils.get_data import Data
from utils.get_model import Model
from utils.get_prediction import Inference

def main():
    with st.sidebar:
        selected = option_menu('About Process',

                            [
                                'EDA - Univariate',
                                'EDA - Bivariate',
                                'Predictive Models',
                                'Model Evaluation'                              
                            ],
                            menu_icon='database-fill-check',
                            icons=['clipboard-pulse', 'chevron-bar-contract', 'boxes'],
                            default_index=0)
    
    st.title("Testosterone Level Checker")
    
    if selected == 'Predictive Models':

        html_temp = """
    <div style="background-color:tomato;padding:10px;margin-bottom:10px;">
    <h2 style="color:white;text-align:center;">Testosterone Deficiency Prediction ML App </h2>
    </div>
    """
        st.markdown(html_temp,unsafe_allow_html=True)


        Age = st.slider('How old are you?', 45, 85, 60)
        st.markdown("""<br>""",unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            TG = st.text_input('Triglycerides (mg/dl)')

        with col2:
            AC = st.text_input('Waist Circumference (cm)')

        HDL = st.text_input('High-Density Lipoprotein levels (mg/dl)')

        st.markdown("""<br>""",unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            HT = st.toggle(' Do you have Hypertension?')
        
        with col2:
            DM = st.toggle('Do you have Diabetes?')

        st.markdown("""<br>""",unsafe_allow_html=True)
        model_name = st.selectbox("Select your AI Doctor!!!", ("SVM", "XGB", "RF", "ANN", "KNN"), index = None, placeholder="Select Doctor...")
        st.write('You selected:', model_name)
        st.markdown("""<br>""",unsafe_allow_html=True)


        # code for Prediction
        Test_result = ''
        # creating a button for Prediction    
        if st.button("Testosterone Deficiency Test Result"):

            # Get data
            data = Data(model_name, Age, DM, TG, HT, HDL, AC).get_data()

            # Get model
            model = Model().get_model(model_name)

            # Prediction
            output = Inference(model,model_name).predict(data)

            # Output
            if output == 1:
                Test_result = "The medical literature suggests that normal testosterone levels range from 300 to 1200 (ng/dl)\nThe person does not have Testosterone Deficiency (Level >= 300 ng/dl)"
            else:
                Test_result = "The medical literature suggests that normal testosterone levels range from 300 to 1200 (ng/dl)\nThe person has Testosterone Deficiency (Level <300 ng/dl)"

            st.success(Test_result)

if __name__=='__main__':
    main()