import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Proyecto Semana Sistemas")
mapa = folium.Map(location=[24.1426, -110.3128], zoom_start=14)

puntos_interes = [
    {"name": "Punto de interes 1", "location": [24.144370, -110.312590]},
    {"name": "Punto de interes 2", "location": [24.142456, -110.313708]},
    {"name": "Punto de interes 3", "location": [24.132456, -110.313708]},
    {"name": "Punto de interes 4", "location": [24.132356, -110.312708]}
]

for punto in puntos_interes:
    folium.Marker(
        location=punto["location"],
        popup=punto["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mapa)

st_folium(mapa, width=725)
