from fastapi import HTTPException
from src.models.appointment_model import Appointment  # Ajusta al nombre real

def cancel_appointment(db, appointment_id):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    db.delete(appointment)
    db.commit()
    return {"message": "Appointment cancelled"}
