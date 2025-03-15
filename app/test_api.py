import requests

# Test Home Route
response = requests.get("http://127.0.0.1:5000/")
print(response.json())

# Test Stock Price Simulation
stock_data = {
    "n_simulations": 1000,
    "n_steps": 10,
    "initial_price": 50,
    "mu": 0.05,
    "sigma": 0.2,
    "time_interval": 1,
    "dividend_yield": 0.02
}
response = requests.post("http://127.0.0.1:5000/simulate-stock", json=stock_data)
print(response.json())

# Test Bond Pricing
bond_data = {
    "yield_to_maturity": 0.05,
    "coupon_rate": 0.08,
    "maturity": 5,
    "periods_per_year": 2,
    "face_value": 1000
}
response = requests.post("http://127.0.0.1:5000/price-bond", json=bond_data)
print(response.json())
