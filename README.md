# 🌦 Chatbot del Clima con Streamlit

Este es un chatbot desarrollado en Python que permite consultar el clima de cualquier ciudad en tiempo real usando la API de OpenWeather.

<img width="841" alt="Captura de pantalla 2025-03-13 a la(s) 6 41 31 p  m" src="https://github.com/user-attachments/assets/79505434-c407-44b4-a878-f56e71d88fcc" />


## 🚀 Características
•⁠  ⁠Consulta el clima de cualquier ciudad.
•⁠  ⁠Muestra la temperatura actual en °C.
•⁠  ⁠Indica la velocidad del viento y una breve descripción del clima.
•⁠  ⁠Interfaz amigable desarrollada con *Streamlit*.

## 📌 Tecnologías utilizadas
•⁠  ⁠*Python 3*
•⁠  ⁠*Streamlit* (para la interfaz)
•⁠  ⁠*OpenWeather API* (para obtener los datos del clima)
•⁠  ⁠*Requests* (para hacer peticiones HTTP)

## 📌 Instalación y aplicación 

# 📌 URL base de la API
url = "https://api.openweathermap.org/data/2.5/weather"

# 📌 Reemplaza "TU_CLAVE_API" con tu clave real de OpenWeather
api_key = "c35d148a8c6481ee8a81fdddced6e4e8"

# 📌 Elige la ciudad que quieres consultar
ciudad = "Madrid"

# 📌 Parámetros para la consulta
params = {
    "q": ciudad,
    "appid": api_key,
    "units": "metric",  # °C
    "lang": "es"  # Español
}

# 📌 Hacer la solicitud GET
response = requests.get(url, params=params)
data = response.json()

# 📌 Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print(f"🌤 Clima en {ciudad}: {data['weather'][0]['description'].capitalize()}")
    print(f"🌡 Temperatura: {data['main']['temp']}°C")
    print(f"💨 Viento: {data['wind']['speed']} m/s")
else:
    print(f"Error: {data.get('message', 'No se pudo obtener el clima')}")

    print(f"Código de respuesta: {response.status_code}")

# 📌 Botón para hacer la solicitud
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


