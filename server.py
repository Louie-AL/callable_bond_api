from flask import Flask, request, jsonify
from flask_cors import CORS
from app.services import calculate_bond_price  # Ensure correct import

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

@app.route('/price-convertible-bond', methods=['POST'])
def price_convertible_bond():
    data = request.json  # Get input data from frontend

    bond_price = calculate_bond_price(
        data["yield_to_maturity"],
        data["coupon_rate"],
        data["maturity"],
        data["periods_per_year"],  # Pass this directly without modifying
        data["face_value"]
    )

    return jsonify({"bond_price": bond_price})

if __name__ == '__main__':
    app.run(debug=True)
