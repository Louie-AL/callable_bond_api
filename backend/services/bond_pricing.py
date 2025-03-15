import numpy as np
from scipy.stats import norm

def generate_gbm(n_simulations, n_steps, initial_price, mu, sigma, time_interval, dividend_yield=0):
    """
    Simulates stock price paths using Geometric Brownian Motion (GBM).
    """
    dt = time_interval / n_steps
    drift = (mu - dividend_yield - 0.5 * sigma ** 2) * dt
    diffusion = sigma * np.sqrt(dt) * np.random.randn(n_simulations, n_steps)
    price_paths = initial_price * np.exp(np.cumsum(drift + diffusion, axis=1))
    
    return price_paths

def bond_price(yield_to_maturity, coupon_rate, maturity, periods_per_year, face_value=100):
    """
    Computes the present value of bond cash flows using discounting.
    """
    periods = int(maturity * periods_per_year)
    discount_factor = (1 + yield_to_maturity / periods_per_year) ** np.arange(1, periods + 1)
    coupon_payment = (coupon_rate * face_value) / periods_per_year
    pv_coupons = np.sum(coupon_payment / discount_factor)
    pv_face_value = face_value / (1 + yield_to_maturity / periods_per_year) ** periods
    return pv_coupons + pv_face_value

def callable_convertible_bond_pricing(initial_price, strike_price, conversion_ratio, call_price, 
                                      n_simulations, n_steps, mu, sigma, time_interval, yield_to_maturity,
                                      coupon_rate, maturity, periods_per_year, face_value):
    """
    Prices a callable convertible bond using Monte Carlo simulation.
    """
    stock_paths = generate_gbm(n_simulations, n_steps, initial_price, mu, sigma, time_interval)
    
    bond_values = np.array([
        bond_price(yield_to_maturity, coupon_rate, maturity, periods_per_year, face_value)
        for _ in range(n_simulations)
    ])
    
    conversion_values = conversion_ratio * stock_paths[:, -1]
    
    final_values = np.maximum(bond_values, conversion_values)
    
    final_values = np.minimum(final_values, call_price)
    
    discount_factor = np.exp(-yield_to_maturity * time_interval)
    present_value = np.mean(final_values) * discount_factor
    
    return present_value
