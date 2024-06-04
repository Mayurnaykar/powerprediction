import streamlit as st
import pickle
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

import seaborn as sns
import matplotlib as plt

# Load the model
with open('power_predict.pkl', 'rb') as file:
    model = pickle.load(file)


# Adding some footer information
st.sidebar.info("U can see different plots of power for different parameters ")



def main():
    st.title("Welcome to ML based power estimation app")

    tech_type = st.selectbox(
        'Select circuit type',
        [ 'Digital Circuits','Microcontrollers', 'Digital Signal Processors']
    )

    st.sidebar.header('Power Prediction')
    house_type = st.selectbox(
        'Select technology type',
        ['180nm', '90nm']
    )
    
    GATE = st.text_input("Enter the total number of gates")
    INV = st.text_input("Enter the number of inverters")
    NAND = st.text_input("Enter the number of NAND gates for the design")
    AND = st.text_input("Enter the number of AND gates for the design")
    NOR = st.text_input("Enter the number of NOR gates for the design")
    OR = st.text_input("Enter the number of OR gates for the design")
    DFF = st.text_input("Enter the number of D flip-flops for the design")
    IN = st.text_input("Enter the number of input terminals for the design")
    OUT = st.text_input("Enter the number of output terminals for the design")
    
    
    param1 = st.sidebar.slider('Clock frequency in MHz', min_value=1, max_value=50, value=25)
    
    if st.button("Predict"):
        input_data = np.array([[GATE, AND, INV, NOR, NAND, OR, DFF, IN, OUT]])
        prediction = model.predict(input_data)
        st.write(f"The predicted power is {prediction[0]:.2f} mW")
        if (prediction<1):
            st.write("Ur good to go for design ") 

    if st.button("graph"):
        tips=pd.read_csv(r"D:\dataset\vlsi dataset with power.csv")
        sns.set(rc={'figure.figsize':(6,4)})
# Sidebar for selecting the chart type
        

# Scatter Plot
        

        st.subheader('line Plot')
        sns.lineplot(data=tips, x="GATE", y="Monte Carlo Simulation power in mw.")
        st.pyplot()

# Line Plot
        
        st.subheader('Scatter Plot')
        sns.scatterplot(data=tips, x="AND", y="Monte Carlo Simulation power in mw.",hue="IN")
        st.pyplot()

        st.subheader('bar plot')
        sns.barplot(data=tips, x='DFF',y='Monte Carlo Simulation power in mw.',hue="OUT")
        st.pyplot()
 
   
if __name__=='__main__':
    main()
