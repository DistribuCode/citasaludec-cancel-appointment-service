from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from prometheus_client import Counter
from src.config.db import SessionLocal
from src.middlewares.auth_middleware import verify_jwt
from src.controllers.appointment_controller import cancel_appointment

router = APIRouter()
appointment_cancel_counter = Counter('appointment_cancellations', 'Number of canceled appointments')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.delete("/appointments/{appointment_id}")
async def cancel(
    appointment_id: int,
    db: Session = Depends(get_db),
    user = Depends(verify_jwt)
):
    # Aquí podrías hacer logs con user["id"], etc
    result = cancel_appointment(db, appointment_id)
    appointment_cancel_counter.inc()
    return result
