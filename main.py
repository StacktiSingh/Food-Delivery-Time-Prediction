from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load your trained Random Forest pipeline
model = joblib.load("random_forest_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        data = {
            "Delivery_person_Age": float(request.form["age"]),
            "Delivery_person_Ratings": float(request.form["rating"]),
            "Vehicle_condition": int(request.form["vehicle_condition"]),
            "multiple_deliveries": int(request.form["multiple_deliveries"]),
            "pickup_delay_min": float(request.form["pickup_delay"]),
            "distance_km": float(request.form["distance"]),
            "order_hour": int(request.form["order_hour"]),
            "picked_hour": int(request.form["picked_hour"]),
            "is_peak_hour": int(request.form["is_peak"]),
            "order_weekday": int(request.form["weekday"]),
            "is_weekend": int(request.form["is_weekend"]),
            "Order_day": int(request.form['order_day']),  # ✅ auto-filled
            "Order_month": int(request.form['order_month']),  # ✅ auto-filled
            "Weatherconditions": request.form["weather"],
            "Road_traffic_density": request.form["traffic"],
            "Type_of_order": request.form["order_type"],
            "Type_of_vehicle": request.form["vehicle_type"],
            "Festival": request.form["festival"],
            "City": request.form["city"],
        }

        # Convert dict into DataFrame (very important)
        input_df = pd.DataFrame([data])

        # Predict using your model pipeline
        prediction = model.predict(input_df)[0]

        # Round delivery time
        predicted_time = round(prediction, 2)

        # Send prediction back to HTML
        return render_template(
            "predict.html",
            prediction_text=f"{predicted_time} minutes",
            delivery_time=predicted_time
        )
    return render_template('predict.html')


if __name__ == "__main__":
    app.run(debug=True)
