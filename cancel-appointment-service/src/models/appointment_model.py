from sqlalchemy import Column, Integer, String
from src.config.db import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, nullable=False)
    date = Column(String, nullable=False)
    status = Column(String, default="scheduled")
