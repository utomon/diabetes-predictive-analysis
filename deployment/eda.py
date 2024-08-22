import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image



def run():

    # make Title
    st.title('Diabetes Health Indicator Prediction')

    # make subheader
    st.subheader('Exploratory Data Analysis to Diabetes Indicators')

    # add image
    image = Image.open('images.png')
    st.image(image, caption = 'Diabetes Check')

    st.write('### What is it?')

    # add description
    st.write(
        "Diabetes is a prevalent chronic disease in the U.S., affecting millions and imposing significant economic costs. It impairs the body's ability to regulate blood glucose levels, leading to serious complications like heart disease and kidney failure. While there is no cure, lifestyle changes and medical treatments can mitigate its impact. Early diagnosis is crucial, yet many remain unaware of their risk. The disease disproportionately affects those of lower socioeconomic status, with total annual costs nearing $400 billion."
        )

    # bold
    st.write('*The Behavioral Risk Factor Surveillance System (BRFSS) is an annual health-related telephone survey by the CDC, collecting data from over 400,000 Americans on health behaviors, chronic conditions, and preventative services since 1984.*')

    # make line
    st.markdown('---')

    st.write('## Dataset')

    #show dataframe
    df = pd.read_csv('/Users/david/Milestone/p1-ftds018-hck-m2-utomon/diabetes_binary_5050split_health_indicators_BRFSS2015.csv')
    st.dataframe(df)

    st.write("The dataset contains 70,692 survey responses to the CDC's BRFSS2015. It has an equal 50-50 split of respondents with no diabetes and with either prediabetes or diabetes. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes")

    st.write("## Visualizations")

    histogram , heatmap , pie_chart = st.tabs(['Histogram' , 'Heatmap' , 'Pie Chart'])


    with histogram:
        st.header('Histogram of Dataset')
        st.write('Histogram of all columns to understand the dataset better.')
        fig, ax = plt.subplots(figsize=(20, 15))
        df.hist(ax=ax)
        st.pyplot(fig)

    with heatmap:
        st.header('Correlation of Features')
        st.write("Using heatmap to understand the dataset better and it's correlation to the target.")
        fig, ax = plt.subplots(figsize=(20, 10))
        sns.heatmap(df.corr(), annot=True, cmap='YlOrRd', ax=ax)
        st.pyplot(fig)

    with pie_chart:
        st.header('Sample of Diabetic and Non-Diabetic People')
        st.write('Simple Pie Chart to visualize that the data is balanced.')
        palette_color = sns.color_palette("Spectral") 
        fig = plt.figure(figsize=(15,5))
        labels=["Non-Diabetic","Diabetic"]
        plt.pie(df["Diabetes_binary"].value_counts() , labels=labels, colors=palette_color, autopct='%.02f%%')
        st.pyplot(fig)




if __name__ == '__main__':
    run()