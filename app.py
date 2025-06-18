from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

# Known cities with real-like sample data
water_data = {
    "New York": {"pH": 7.4, "temperature": 22.5, "turbidity": 5.1, "status": "Safe"},
    "Mumbai": {"pH": 6.9, "temperature": 26.1, "turbidity": 4.3, "status": "Moderate"},
    "London": {"pH": 7.1, "temperature": 18.2, "turbidity": 2.8, "status": "Safe"},
    "Kathmandu": {"pH": 6.7, "temperature": 20.0, "turbidity": 3.5, "status": "Moderate"},
    "Tokyo": {"pH": 7.2, "temperature": 19.5, "turbidity": 3.0, "status": "Safe"},
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/water-quality", methods=["GET"])
def get_water_quality():
    place = request.args.get("place")
    if not place:
        return jsonify({"error": "No place provided"}), 400

    place_cap = place.title()  # Normalize e.g., "kathmandu" => "Kathmandu"
    data = water_data.get(place_cap)

    if data:
        return jsonify({"place": place_cap, "data": data})
    else:
        # Generate estimated fake data
        estimated_data = {
            "pH": round(random.uniform(6.5, 8.5), 1),
            "temperature": round(random.uniform(15, 30), 1),
            "turbidity": round(random.uniform(1, 10), 1),
            "status": "Estimated"
        }
        return jsonify({
            "place": place_cap,
            "data": estimated_data,
            "note": "This is estimated data. Real-time data not available for this location."
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

