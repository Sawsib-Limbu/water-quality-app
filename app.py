from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample data
water_data = {
    "New York": {"pH": 7.4, "temperature": 22.5, "turbidity": 5.1, "status": "Safe"},
    "Mumbai": {"pH": 6.9, "temperature": 26.1, "turbidity": 4.3, "status": "Moderate"},
    "London": {"pH": 7.1, "temperature": 18.2, "turbidity": 2.8, "status": "Safe"},
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/water-quality", methods=["GET"])
def get_water_quality():
    place = request.args.get("place")
    data = water_data.get(place)
    if data:
        return jsonify({"place": place, "data": data})
    else:
        return jsonify({"error": f"No data found for {place}"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

