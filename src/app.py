import streamlit as st
import streamlit_folium as st_map
from src import proximity_map as map

def display_map(address):
    m = map.generate_proximity_map(address)
    return st_map.st_folium(m)

if 'address_input' not in st.session_state:
    st.session_state.address_input = None 

address = st.text_input(label="Address", key="address_input")


button = st.button(label="Submit", key="address_submit", on_click=display_map, args=[address])