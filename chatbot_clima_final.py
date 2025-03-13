from flask import Flask, jsonify, request
import requests

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# URL de la API de clima (reemplaza esto con tu propia API si ya tienes una)
CLIMA_API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "TU_API_KEY"  # Reemplaza con tu propia API Key de OpenWeatherMap

# Endpoint para obtener el clima de una ciudad
@app.route('/clima', methods=['GET'])
def clima():
    # Obtener el parámetro 'ciudad' desde la URL
    ciudad = request.args.get('ciudad', 'Madrid')  # Si no se proporciona, por defecto será Madrid
    
    # Consultar la API del clima
    params = {
        'q': ciudad,
        'appid': API_KEY,
        'units': 'metric',  # Para obtener la temperatura en grados Celsius
        'lang': 'es'  # Idioma de la respuesta
    }

    response = requests.get(CLIMA_API_URL, params=params)
    data = response.json()

    # Verificar si la respuesta es válida
    if response.status_code == 200:
        clima_data = {
            "ciudad": data['name'],
            "pais": data['sys']['country'],
            "temperatura": data['main']['temp'],
            "descripcion": data['weather'][0]['description'],
            "humedad": data['main']['humidity'],
            "viento": data['wind']['speed']
        }
        return jsonify(clima_data)
    else:
        return jsonify({"error": "No se pudo obtener los datos del clima."}), 400

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5000)