import streamlit as st

def main():
    st.title("Power Prediction App")

    # Input fields
    input1 = st.text_input("Enter the number of and gates used", "")
    input2 = st.text_input("Enter the number of or gates used", "")
    input3 = st.text_input("Enter the number of nand gates used", "")
    input4 = st.text_input("Enter the number of nor gates used", "")
    input5 = st.text_input("Enter the number of input pins used", "")
    input6 = st.text_input("Enter the number of output pins used", "")
    input7 = st.text_input("Enter the number of inverters", "")
    input8 = st.text_input("Enter the number of DFFs", "")
    
    # Button to trigger prediction
    if st.button("Predict"):
        if input1 and input2 and input3 and input4 and input5 and input6 and input7 and input8:
            st.write("Enter the number of and gates used:", input1)
            st.write("Enter the number of or gates used:", input2)
            st.write("Enter the number of nand gates used:", input3)
            st.write("Enter the number of nor gates used:", input4)
            st.write("Enter the number of input pins used:", input5)
            st.write("Enter the number of output pins used:", input6)
            st.write("Enter the number of inverters used:", input7)
            st.write("Enter the number of DFFs used:", input8)
            # Add your prediction logic here
        else:
            st.warning("Please fill in all input fields")

if __name__ == "__main__":
    main()
    