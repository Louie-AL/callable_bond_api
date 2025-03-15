import numpy as np

def generate_gbm(n_simulations, n_steps, initial_price, mu, sigma, time_interval, dividend_yield):
    dt = time_interval / n_steps
    sqrt_dt = np.sqrt(dt)
    stock_prices = np.zeros((n_simulations, n_steps + 1))
    stock_prices[:, 0] = initial_price
    for i in range(1, n_steps + 1):
        random_numbers = np.random.normal(0, 1, size=n_simulations)
        stock_prices[:, i] = stock_prices[:, i - 1] * np.exp(
            (mu - dividend_yield - 0.5 * sigma ** 2) * dt + sigma * sqrt_dt * random_numbers
        )
    return stock_prices

def calculate_bond_price(yield_to_maturity, coupon_rate, maturity, periods_per_year, face_value):
    r = yield_to_maturity / periods_per_year
    n = int(maturity * periods_per_year)
    time_points = np.linspace(0, maturity, num=n + 1)
    bond_prices = np.zeros(n + 1)

    for i in range(1, n + 1):
        t = time_points[i]
        pv_coupons = (coupon_rate * face_value / periods_per_year) * np.exp(-r * t)
        pv_face_value = face_value * np.exp(-r * t) if t == time_points[-1] else 0
        bond_prices[i] = pv_coupons + pv_face_value

    return np.sum(bond_prices)

