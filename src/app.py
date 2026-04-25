import streamlit as st
from streamlit_folium import st_folium
from src import proximity_map as map, proximity_analyzer as prox

if 'address_input' not in st.session_state:
    st.session_state.address_input = None
if 'closest_stream_result' not in st.session_state:
    st.session_state.closest_stream_result = None
if 'submit_clicked' not in st.session_state:
    st.session_state.submit_clicked = False

def display_map():
    st.session_state.submit_clicked = True
    
st.title("Trout Stream Proximity Tool")

st.text_input(label="Address", key="address_input")

st.button(label="Submit", key="address_submit", on_click=display_map)

results = st.container(key="results_container")

if st.session_state.submit_clicked == True and len(st.session_state.address_input) > 0:
    st.session_state.closest_stream_result = prox.return_closest_stream(st.session_state.address_input)

if st.session_state.closest_stream_result != None:
    msg = [f"The Class A trout stream nearest to __**{st.session_state.closest_stream_result["address"]}**__ is:",
        f"**{st.session_state.closest_stream_result["nearest_stream_name"]}**, which is",
        f"{st.session_state.closest_stream_result["nearest_stream_distance_miles"]} mile(s) away."]
    result_info = "\n".join(msg)
    results.markdown(result_info)
    
    m = map.generate_proximity_map(st.session_state.closest_stream_result)
    st_folium(m, width=750)