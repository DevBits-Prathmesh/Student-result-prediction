import streamlit as st
import pandas as pd
import joblib
import os
st.set_page_config(page_title='PASS OR FAIL',page_icon='👀')
def load_model(model_path):
    try:
        model_path=model_path.replace('\\','/')
        if not os.path.exists(model_path):
            st.error(f'File does not exits{model_path}')
            return None
        return joblib.load(model_path)
    except Exception as e:
        st.error(f'Error Loading Model: {str(e)}')
        return None
with st.spinner('loading model'):
    student=load_model("student_model")
if student is None:
    st.error('model not found')
    st.stop()
#ui generation
st.title('PASS OR FAIL !!')
st.subheader('According To Hardwork,Predict Student Result !')
st.text('Predict student Pass or Fail according to following Properties')
with st.form('form'):
    hour=st.number_input('How Many Hours Do you Study Daily')
    attendance=st.number_input('Attendence out 100%')
    previous=st.slider('Previous Grades')
    submit=st.form_submit_button('Predict')
if submit:
    input_data=pd.DataFrame([{
        'Study_Hours':int(hour),
        'Attendance':attendance,
        'Previous_Grade':previous
    }])
try:
    with st.spinner('precessing..'):
        pred=student.predict(input_data)[0]
        re='PASS' if pred == 1 else 'FAIL'
        st.success(f'The Student will "{re}"')
except Exception as e:
    st.error(f'Prediction Field{str(e)}')