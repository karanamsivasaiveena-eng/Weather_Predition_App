from flask import Flask, render_template, request
import requests
from model import predict_temperature

app = Flask(__name__)

API_KEY = "660a5dcd09d62cc729b9e642e7a6bc4e"   # 🔴 Put your real key here

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    prediction = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        print(data)  # 👈 DEBUG (see what's coming)

        # ✅ CORRECT handling
        if str(data.get("cod")) == "200":
            weather_data = {
                "city": data.get("name"),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "description": data["weather"][0]["description"]
            }

            prediction = predict_temperature(weather_data["temperature"])

        else:
            # 🔥 Show real API message instead of generic error
            weather_data = {
                "error": data.get("message", "Something went wrong")
            }

    return render_template("index.html", weather=weather_data, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=False)