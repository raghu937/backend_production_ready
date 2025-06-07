from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import chat as chat_model
from app.models import interest as interest_model
from app.database import get_db

router = APIRouter(prefix="/chat", tags=["chat"])

def check_mutual_match(sender_id: int, receiver_id: int, db: Session):
    # Check if both accepted each other
    sent = db.query(interest_model.Interest).filter(
        interest_model.Interest.sender_id == sender_id,
        interest_model.Interest.receiver_id == receiver_id,
        interest_model.Interest.status == "accepted"
    ).first()
    received = db.query(interest_model.Interest).filter(
        interest_model.Interest.sender_id == receiver_id,
        interest_model.Interest.receiver_id == sender_id,
        interest_model.Interest.status == "accepted"
    ).first()
    return sent and received

@router.post("/send")
def send_message(sender_id: int, receiver_id: int, message: str, db: Session = Depends(get_db)):
    if not check_mutual_match(sender_id, receiver_id, db):
        raise HTTPException(status_code=403, detail="Chat not allowed without mutual acceptance")
    chat_msg = chat_model.ChatMessage(sender_id=sender_id, receiver_id=receiver_id, message=message)
    db.add(chat_msg)
    db.commit()
    db.refresh(chat_msg)
    return {"msg": "Message sent", "chat_id": chat_msg.id}

@router.get("/history/{user1_id}/{user2_id}")
def get_chat_history(user1_id: int, user2_id: int, db: Session = Depends(get_db)):
    chats = db.query(chat_model.ChatMessage).filter(
        ((chat_model.ChatMessage.sender_id == user1_id) & (chat_model.ChatMessage.receiver_id == user2_id)) |
        ((chat_model.ChatMessage.sender_id == user2_id) & (chat_model.ChatMessage.receiver_id == user1_id))
    ).order_by(chat_model.ChatMessage.timestamp).all()
    return chats