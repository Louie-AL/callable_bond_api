from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from backend.database import init_db  # Import init_db
from backend.services.bond_pricing import callable_convertible_bond_pricing, bond_price, generate_gbm
from flask import jsonify
import logging

logging.basicConfig(level=logging.DEBUG, force=True)

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Ensure database tables are created when Flask starts
init_db()

@app.route("/")
def home():
    return jsonify({"message": "Callable Bond Pricing API is running!"})

@app.route("/simulate-stock", methods=["POST"])
def simulate_stock():
    data = request.json
    stock_paths = generate_gbm(
        n_simulations=data["n_simulations"],
        n_steps=data["n_steps"],
        initial_price=data["initial_price"],
        mu=data["mu"],
        sigma=data["sigma"],
        time_interval=data["time_interval"],
        dividend_yield=data.get("dividend_yield", 0)
    )
    return jsonify({"simulated_stock_prices": stock_paths.tolist()})

@app.route("/price-bond", methods=["POST"])
def price_bond():
    data = request.json
    price = bond_price(
        yield_to_maturity=data["yield_to_maturity"],
        coupon_rate=data["coupon_rate"],
        maturity=data["maturity"],
        periods_per_year=data["periods_per_year"],
        face_value=data.get("face_value", 100)
    )
    return jsonify({"bond_price": price})

@app.route("/price-convertible-bond", methods=["POST"])
def price_convertible_bond():
    data = request.json
    price = callable_convertible_bond_pricing(
        initial_price=data["initial_price"],
        strike_price=data["strike_price"],
        conversion_ratio=data["conversion_ratio"],
        call_price=data["call_price"],
        n_simulations=data["n_simulations"],
        n_steps=data["n_steps"],
        mu=data["mu"],
        sigma=data["sigma"],
        time_interval=data["time_interval"],
        yield_to_maturity=data["yield_to_maturity"],
        coupon_rate=data["coupon_rate"],
        maturity=data["maturity"],
        periods_per_year=data["periods_per_year"],
        face_value=data.get("face_value", 100)
    )
    return jsonify({"convertible_bond_price": price})

#error handling

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
