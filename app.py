from flask import Flask, request, render_template
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    try:
        data = [float(request.form.get(k)) for k in [
            'Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH', 'Rainfall']]
        scaled_data = sc.transform([data])
        prediction = model.predict(scaled_data)

        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        crop_name = crop_dict.get(prediction[0], "Unknown Crop")
        result = f"{crop_name} is the best crop to cultivate."

        return render_template("index.html", result=result)

    except Exception as e:
        return render_template("index.html", result="Error: " + str(e))


if __name__ == "__main__":
    app.run(debug=True)
