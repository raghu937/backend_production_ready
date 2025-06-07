from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import stripe
from app.models import payment as payment_model
from app.database import get_db

router = APIRouter(prefix="/payments", tags=["payments"])

stripe.api_key = "your_stripe_secret_key"  # Replace with your Stripe Secret Key

@router.post("/create-checkout-session")
def create_checkout_session(user_id: int, plan: str, db: Session = Depends(get_db)):
    if plan not in ["Gold", "Platinum"]:
        raise HTTPException(status_code=400, detail="Invalid Plan")

    amount = 5000 if plan == "Gold" else 8000  # 5000 = Rs. 50, 8000 = Rs. 80 (in paisa)

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': f'{plan} Membership',
                    },
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        payment = payment_model.Payment(user_id=user_id, plan=plan, stripe_payment_intent=session.payment_intent)
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return {"checkout_url": session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))