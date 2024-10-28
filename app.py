import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Proyecto Semana Sistemas")
mapa = folium.Map(location=[24.1426, -110.3128], zoom_start=14)

puntos_interes = [
    {"name": "Doce Cuarenta", "location": [23.4558175, -110.2212408]},
    {"name": "Catedral", "location": [-34.60757, -58.3742905]}
]

for punto in puntos_interes:
    folium.Marker(
        location=punto["location"],
        popup=punto["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mapa)

st_folium(mapa, width=725)
