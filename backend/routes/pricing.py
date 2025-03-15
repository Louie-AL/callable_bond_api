import logging
from fastapi import APIRouter
from backend.database import SessionLocal
from backend.models import BondPriceResult
from backend.services.bond_pricing import callable_convertible_bond_pricing

logging.basicConfig(level=logging.DEBUG)

router = APIRouter()

print("🚀 Pricing API Loaded")

@router.post("/price-convertible-bond")
def price_convertible_bond(data: dict):
    logging.debug("🚀 Received API request with data:")
    logging.debug(data)

    computed_price = callable_convertible_bond_pricing(
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
        face_value=data["face_value"]
    )

    logging.debug(f"✅ Computed Bond Price: {computed_price}")

    # ✅ Check if database session is being called
    db = SessionLocal()
    try:
        logging.debug("📌 Creating bond entry...")
        bond_entry = BondPriceResult(
            bond_type="Convertible",
            initial_price=data["initial_price"],
            strike_price=data["strike_price"],
            conversion_ratio=data["conversion_ratio"],
            call_price=data["call_price"],
            maturity=data["maturity"],
            yield_to_maturity=data["yield_to_maturity"],
            computed_price=computed_price
        )

        logging.debug("📌 Adding bond entry to database...")
        db.add(bond_entry)

        logging.debug("📌 Committing changes to database...")
        db.commit()

        logging.debug("📌 Refreshing bond entry...")
        db.refresh(bond_entry)

        logging.debug(f"✅ Bond entry saved with ID: {bond_entry.id}")

        return {"convertible_bond_price": computed_price, "id": bond_entry.id}

    except Exception as e:
        db.rollback()
        logging.error(f"❌ Database error: {e}")
        return {"error": "Failed to save data"}
    finally:
        db.close()
        logging.debug("✅ Database session closed.")
