import streamlit as st
import pickle
import json
import pandas as pd
import numpy as np

# Load Files
with open('model_rf.pkl', 'rb') as file_1:
   model_rf = pickle.load(file_1)


def run():
   with st.form('form_Diabetes'):
      
        HighBP = st.selectbox('High Blood Pressure', [0 , 1], index= 1 , help= "Do you have high Blood Pressure?")
        HighChol = st.selectbox('High Cholestrol' , [0 , 1], index = 1 , help= "Do you have high Cholestrol?")
        CholCheck = st.selectbox('Cholestrol Check' , [0 , 1], index = 1 , help= "Have you had a Cholestrol Check in the past 5 years?")
        BMI = st.slider('BMI' , 0, 180 , 18)
        Smoker = st.selectbox('Smoker' , [0 , 1], index = 1 , help= "Do you Smoke?")
        Stroke = st.selectbox('Stroke' , [0 , 1], index = 1 , help= "Ever had a stroke?")
        HeartDiseaseorAttack = st.selectbox('HeartDiseaseorAttack' , [0 , 1], index = 1, help= "Do you hve coronary heart disease")
        PhysActivity = st.selectbox('PhysActivity' , [0 , 1], index = 1, help = "physical activity in past 30 days - not including job")
        Fruits = st.selectbox('Fruits' , [0 , 1], index = 1, help="Consume Fruit 1 or more times per day")
        Veggies = st.selectbox('Veggies' , [0 , 1], index = 1 , help="Consume Vegetables 1 or more times per day")
        HvyAlcoholConsump = st.selectbox('HvyAlcoholConsump' , [0 , 1], index = 1 , help="Are you a heavy drinker?")
        AnyHealthcare = st.selectbox('AnyHealthcare' , [0 , 1], index = 1, help="Have any kind of health care coverage, including health insurance")
        NoDocbcCost = st.selectbox('NoDocbcCost' , [0 , 1], index = 1, help="Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?")
        GenHlth = st.slider('GenHlth' , 1, 5 , 1, help="Would you say that in general your health is? 1 is excellemt and 5 is poor")
        MentHlth = st.slider('MenHlth' , 0, 30 , 1, help="days of poor mental health scale 1-30 days")
        PhysHlth = st.slider('PhysHlth' , 0, 30 , 1 , help="physical illness or injury days in past 30 days scale 1-30")
        DiffWalk = st.selectbox('DiffWalk' , [0 , 1], index = 1, help="Do you have serious difficulty walking or climbing stairs?")
        Sex = st.selectbox('Sex' , [0 , 1], index = 1, help="0 is female , 1 is male")
        Age = st.slider('Age' , 0, 100 , 1)
        Education = st.slider('Education' , 1, 6 , 1)
        Income = st.slider('Income' , 1, 8 , 1)




        #submit button
        submitted = st.form_submit_button('Predict')

        data_inf = {
            'HighBP' : HighBP,
            'HighChol' : HighChol,
            'CholCheck' : CholCheck,
            'BMI' : BMI,
            'Smoker' : Smoker,
            'Stroke' : Stroke,
            'HeartDiseaseorAttack' : HeartDiseaseorAttack,
            'PhysActivity' : PhysActivity,
            'Fruits' : Fruits,
            'Veggies' : Veggies,
            'HvyAlcoholConsump' : HvyAlcoholConsump,
            'AnyHealthcare' : AnyHealthcare,
            'NoDocbcCost' : NoDocbcCost,
            'GenHlth' : GenHlth,
            'MentHlth' : MentHlth,
            'PhysHlth' : PhysHlth,
            'DiffWalk' : DiffWalk,
            'Sex' : Sex,
            'Age' : Age,
            'Education' : Education,
            'Income' : Income
            }
        


        data_inf = pd.DataFrame([data_inf])


        if submitted:

            # predict model
            infery_pred_final = model_rf.predict(data_inf)

            # show dataframe result
            st.write(data_inf)
            

            #show predicted result
            st.write('### Prediction Result on Diabetes:', str(int(infery_pred_final)))


if __name__ == '__main__':
    run()

