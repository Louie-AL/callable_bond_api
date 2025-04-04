
# Callable Bond API

This project is a Flask-based API for simulating financial instruments and pricing callable and convertible bonds using Monte Carlo methods. It is designed to support integration with front-end interfaces or other systems that require access to advanced bond pricing computations.

---

## 🚀 Features

- Health check endpoint
- Monte Carlo simulation of stock prices
- Callable bond valuation
- Convertible bond valuation
- Modular and extensible code structure

---

## 📁 Project Structure

```
.
├── app/                    # Core logic for pricing and simulations
├── backend/                # API route definitions and handlers
├── callable_bond_ui/       # (Optional) Front-end or UI-related code
├── run.py                  # App entry point
├── config.py               # Configuration file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📦 Setup

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/Louie-AL/callable_bond_api.git
cd callable_bond_api
pip install -r requirements.txt
```

### Running the API

```bash
python run.py
```

The server will start at `http://localhost:5000`.

---

## 🔁 API Endpoints

### Health Check

**GET /**  
Returns a simple message confirming the API is live.

```json
{ "message": "Callable Bond Pricing API is running!" }
```

---

### Simulate Stock Price

**POST /simulate-stock**

Simulates stock price paths using geometric Brownian motion.

**Request Body:**

```json
{
  "n_simulations": 1000,
  "n_steps": 252,
  "initial_price": 100,
  "mu": 0.07,
  "sigma": 0.2,
  "time_interval": 1
}
```

**Response:**

A JSON object containing simulated price paths.

---

### [Planned] Price Callable Bond

**POST /price-callable-bond**

(Coming Soon) Prices a callable bond based on simulated interest rates and call schedule.

---

### [Planned] Price Convertible Bond

**POST /price-convertible-bond**

(Coming Soon) Prices a convertible bond using stock simulation and bond cash flows.

---

## 🛠 Technologies

- Python
- Flask
- NumPy / SciPy / Pandas
- Monte Carlo Simulation

---

## 📈 Future Work

- Add support for stochastic interest rate models (e.g., CIR, Hull-White)
- Expand convertible bond pricing logic
- Front-end integration (via React or similar)
- Docker support

---

## 🤝 Contributions

Contributions and suggestions are welcome! Feel free to open an issue or pull request.

---

## 📄 License

MIT License

---

## 🧠 Author

- **Louie A.L.**

Reach out on GitHub or LinkedIn for collaboration or questions.
