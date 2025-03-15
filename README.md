# Callable Bond Pricing API

## Overview
This Flask API provides endpoints for stock price simulation, bond pricing, and convertible bond pricing.

## API Endpoints

### 1. Health Check
**GET** `/`
- **Response:** `{ "message": "Callable Bond Pricing API is running!" }`

### 2. Simulate Stock Price
**POST** `/simulate-stock`
- **Request Body:**
```json
{
  "n_simulations": 100,
  "n_steps": 50,
  "initial_price": 100,
  "mu": 0.05,
  "sigma": 0.2,
  "time_interval": 1
}

