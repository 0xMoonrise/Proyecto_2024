#!/usr/bin/env python
from geopy.geocoders import Nominatim
import sys
geolocator = Nominatim(user_agent="mi_app_geopy")
lugar = sys.argv[1]
ubicacion = geolocator.geocode(lugar)

if ubicacion:
    print(f"Coordenadas de {lugar}: ({ubicacion.latitude}, {ubicacion.longitude})")
else:
    print("No se encontraron coordenadas para este lugar.")
