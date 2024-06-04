import streamlit as st
import pickle
import numpy as np



with open('power_predict.pkl', 'rb') as file:
    model = pickle.load(file)

def main():
    st.title("ML based power prediction model")

    tech_type = st.selectbox(
    'Select circuit type',
    ['CPU', 'Microcontrollers', 'MSP430', 'Digital Signal Processors','ASIC','GPU'])

    st.sidebar.header('power prediction')
    house_type = st.selectbox(
    'Select technology type',
    ['180nm', '90nm', '45nm', '32nm'])
    GATE=st.text_input("enter the number of gates")
    INV=st.text_input("enter the number of inverters")
    NAND=st.text_input("enter the number of nand gates")
    AND =st.text_input("enter the number of and gates")
    NOR=st.text_input("enter the number of nor gates")
    OR=st.text_input("enter the number of or gates")
    IN=st.text_input("enter no.of input terminals")
    OUT=st.text_input("enter the number of output terminals")
    DFF=st.text_input("enter the number of D ffs")
    
   
    
    st.sidebar.header('')

# Add sliders in the sidebar for user input
    param1 = st.sidebar.slider('clock frequency in Mhz', min_value=1, max_value=100, value=50)
    #result=""
    if st.button("predict"):
        #result=loaded_model.predict([[GATE,INV,NAND,AND,NOR,OR,IN,OUT]])
        input_data = np.array([[GATE,AND,INV,NOR,NAND,OR,DFF,IN,OUT]])
      
        prediction = model.predict(input_data)
        st.write("The predicted power is in mW",prediction)
   
if __name__=='__main__':
    main()
