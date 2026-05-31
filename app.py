from flask import Flask, render_template, request
import requests
import os
from model import predict_temperature

app = Flask(__name__)

API_KEY = "660a5dcd09d62cc729b9e642e7a6bc4e"

@app.route("/", methods=["GET", "POST"])
def index():

    weather_data = None
    prediction = None

    if request.method == "POST":

        city = request.form.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:

            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "description": data["weather"][0]["description"]
            }

            prediction = predict_temperature(
                weather_data["temperature"]
            )

        else:

            weather_data = {
                "error": data.get(
                    "message",
                    "City not found"
                )
            }

    return render_template(
        "index.html",
        weather=weather_data,
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=False)