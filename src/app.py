import streamlit as st
import streamlit_folium as st_map
from src import proximity_map as map

if 'address_input' not in st.session_state:
    st.session_state.address_input = None
if 'submit_clicked' not in st.session_state:
    st.session_state.submit_clicked = False

def display_map():
    st.session_state.submit_clicked = True
    
st.text_input(label="Address", key="address_input")

st.button(label="Submit", key="address_submit", on_click=display_map)

if st.session_state.submit_clicked == True:
    m = map.generate_proximity_map(st.session_state.address_input)
    st_map.st_folium(m)