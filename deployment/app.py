import streamlit as st
import eda
import prediction

#make sidemenu bar
page = st.sidebar.selectbox('Choose Page', ['EDA' , 'Prediction'])


if page == 'EDA':
    eda.run()
else:
    prediction.run()