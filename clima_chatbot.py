# -*- coding: utf-8 -*-
"""CLIMA

Original file is located at
    https://colab.research.google.com/drive/10CAbzrVd2posFoXFQ-5hgnJ3PrPOeMAB
"""

import requests

# URL base de la API
url = "https://api.openweathermap.org/data/2.5/weather"

# Reemplaza "TU_CLAVE_API" con tu clave real de OpenWeather
api_key = "c35d148a8c6481ee8a81fdddced6e4e8"

# Elige la ciudad que quieres consultar
ciudad = "Madrid"

# Parámetros para la consulta
params = {
    "q": ciudad,
    "appid": api_key,
    "units": "metric",  # °C
    "lang": "es"  # Español
}

# Hacer la solicitud GET
response = requests.get(url, params=params)
data = response.json()

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print(f"🌤 Clima en {ciudad}: {data['weather'][0]['description'].capitalize()}")
    print(f"🌡 Temperatura: {data['main']['temp']}°C")
    print(f"💨 Viento: {data['wind']['speed']} m/s")
else:
    print(f"Error: {data.get('message', 'No se pudo obtener el clima')}")

    print(f"Código de respuesta: {response.status_code}")



import streamlit as st
import requests

# URL base de la API
url = "https://api.openweathermap.org/data/2.5/weather"

# Reemplaza "TU_CLAVE_API" con tu clave real de OpenWeather
api_key = "c35d148a8c6481ee8a81fdddced6e4e8"  # Asegúrate de colocar tu clave aquí

# Título de la app
st.title("🌦 Chatbot del Clima 🌦")

# Solicitar ciudad al usuario
ciudad = st.text_input("¿En qué ciudad quieres conocer el clima?", "Madrid")

# Parámetros para la consulta
params = {
    "q": ciudad,
    "appid": api_key,
    "units": "metric",  # °C
    "lang": "es"  # Español
}

# Botón para hacer la solicitud
if st.button("Consultar clima"):
    response = requests.get(url, params=params)
    data = response.json()

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Mostrar los resultados
        st.write(f"🌤 **Clima en {ciudad}:** {data['weather'][0]['description'].capitalize()}")
        st.write(f"🌡 **Temperatura:** {data['main']['temp']}°C")
        st.write(f"💨 **Viento:** {data['wind']['speed']} m/s")
    else:
        # Mostrar mensaje de error
        st.error(f"❌ Error: {data.get('message', 'No se pudo obtener el clima')}")
        st.write(f"Código de respuesta: {response.status_code}")