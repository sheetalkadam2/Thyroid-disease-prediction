import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

Thyroid_disease_model = pickle.load(open('Thyroid_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Thyroid Disease Prediction System',
                          
                          ['Thyroid Disease Prediction'],
                          icons=['Thyroid'],
                          default_index=0)
    
# Thyroid Disease Prediction Page
if (selected == 'Thyroid Disease Prediction'):
    
    # page title
    st.title('Thyroid Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        on thyroxine = st.text_input('thyroxine')
        
    with col1:
        qot= st.text_input('query on thyroxine')
        
    with col2:
        anti medi = st.text_input('on antithyroid medication')
        
    with col3:
        sk = st.text_input('sick')
        
    with col1:
        pregnant = st.text_input('pregnant')
        
    with col2:
        thyroid surgery = st.text_input('thyroid surgery')
        
    with col3:
       I131 treatment = st.text_input('I131 treatment')
        
    with col1:
       query hypothyroid = st.text_input('query hypothyroid')
        
    with col2:
        query hyperthyroid = st.text_input('query hyperthyroid')
        
    with col3:
        lithium = st.text_input('lithium')
        
    with col1:
        goitre = st.text_input('goitre')

    with col2:
        tumor = st.text_input('tumor')
    
    with col3:
      hypopituitary = st.text_input('I131 treatment')
     
    with col1:
        psych = st.text_input('psych')
   
     with col2:
        TSH = st.text_input('TSH')
     
     with col3:
      T3 = st.text_input('T3')
    
     with col1:
        FTI = st.text_input('FTI') 
     

        
        
     
     
    # code for Prediction
    Thyroid_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Thyroid Disease Test Result'):
        Thyroid_prediction = Thyroid_disease_model.predict([[age, sex, on thyroxine,query on thyroxine, on antithyroid medication, sick,pregnant,thyroid surgery,I131 treatment, query hypothyroid ,query hyperthyroid ,lithium, goitre,tumor,hypopituitary,psych,TSH ,T3,FTI ]])                          
        
        if (Thyroid_prediction[0] == 1):
          Thyroid_diagnosis = 'The person is having Thyroid disease'
        else:
          Thyroid_diagnosis = 'The person does not have any Thyroid disease'
        
    st.success(Thyroid_diagnosis)
        