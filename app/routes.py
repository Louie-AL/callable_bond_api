from flask import Blueprint, request, jsonify

# Import your models and services
from app.models import db, BondPricing
from app.services import generate_gbm, calculate_bond_price

# Define a Blueprint for your API
bp = Blueprint("api", __name__)

# ✅ Add a default home route
@bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Callable Convertible Bond Pricing API is running!"})

# Endpoint to simulate stock prices
@bp.route("/simulate-stock", methods=["POST"])
def simulate_stock():
    data = request.json
    stock_prices = generate_gbm(**data)
    return jsonify({"stock_prices": stock_prices.tolist()})

# Endpoint to calculate bond price
@bp.route("/price-bond", methods=["POST"])
def price_bond():
    data = request.json
    bond_price = calculate_bond_price(**data)
    return jsonify({"bond_price": bond_price})
