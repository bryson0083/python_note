# https://discuss.streamlit.io/t/depdendant-selectbox/17260/4
import streamlit as st

dummy_data = {
    'Man1':['1','111','1111'],
    'Man2':['2','222','22222'],
    'Man3':['3','333','33333'],
}

if __name__ == "__main__":
    # adding "select" as the first and default choice
    manufacturer = st.selectbox('Select Manufacturer', options=['select']+list(dummy_data.keys()))
    # display selectbox 2 if manufacturer is not "select"
    if manufacturer != 'select':
        model_number = st.selectbox('Select Model Number', options=dummy_data[manufacturer])
    if st.button('Submit'):
        st.write('You selected ' + manufacturer + ' ' + model_number)