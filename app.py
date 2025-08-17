from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import os

# ----------------------------
# Config
# ----------------------------
SLA_HOURS = 72  # change if your business SLA is different

# Label encoding note:
# In your notebook you used LabelEncoder() which sorts classes alphabetically.
# For "Flight", "Road", "Ship" that usually maps to: Flight=0, Road=1, Ship=2
# If your classes differ, update the mapping below accordingly.
MODE_MAP = {"Flight": 0, "Road": 1, "Ship": 2}

# ----------------------------
# App & Model
# ----------------------------
app = Flask(__name__)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "delivery_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ----------------------------
# Routes
# ----------------------------
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", sla_hours=SLA_HOURS)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read JSON (fetch) or form (HTML) seamlessly
        if request.is_json:
            payload = request.get_json()
            mode = payload.get("mode_of_shipment")
            cost = float(payload.get("cost_of_the_product"))
            discount = float(payload.get("discount_offered"))
            weight = float(payload.get("weight_in_gms"))
        else:
            mode = request.form.get("mode_of_shipment")
            cost = float(request.form.get("cost_of_the_product"))
            discount = float(request.form.get("discount_offered"))
            weight = float(request.form.get("weight_in_gms"))

        if mode not in MODE_MAP:
            return jsonify({"error": f"Invalid mode_of_shipment: {mode}"}), 400

        mode_val = MODE_MAP[mode]

        # Order of features must match training:
        features = np.array([[mode_val, cost, discount, weight]])

        eta_hours = float(model.predict(features)[0])  # regression prediction
        eta_days = round(eta_hours / 24.0, 2)

        delayed = eta_hours > SLA_HOURS
        delay_hours = max(0.0, eta_hours - SLA_HOURS)

        result = {
            "eta_hours": round(eta_hours, 2),
            "eta_days": eta_days,
            "sla_hours": SLA_HOURS,
            "delayed": bool(delayed),
            "delay_hours": round(delay_hours, 2),
            "mode_of_shipment": mode,
            "cost_of_the_product": cost,
            "discount_offered": discount,
            "weight_in_gms": weight,
        }

        # If AJAX fetch, return JSON; otherwise render HTML
        if request.is_json:
            return jsonify(result)
        else:
            return render_template("index.html", result=result, sla_hours=SLA_HOURS)

    except Exception as e:
        return render_template("index.html", error=str(e), sla_hours=SLA_HOURS), 500

if __name__ == "__main__":
    app.run(debug=True)
