from sqlalchemy import Column, Integer, String,Date
from database import Base 

class PhonebookDB(Base):
    __tablename__ = 'phone_book_tbl'
    participant_id = Column(Integer, primary_key=True)
    first_name = Column(String(256))
    last_name = Column(String(256))
    rut_id = Column(String(256))
    phone_number = Column(String(256))
    qr_code_scanmevacuno = Column(String(512))
    created_datetime = Column(Date)
    qr_code_registrocivil = Column(String(512))

class EventDB(Base):
    __tablename__ = 'event_tbl'
    event_id = Column(Integer, primary_key=True)
    event_name = Column(String(256))
    event_location = Column(String(256))
    register_code = Column(String(256))
    export_code = Column(String(256))
    qr_code_scanmevacuno = Column(String(512))
    created_datetime = Column(Date)
    qr_code_registrocivil = Column(String(512))

class ParticipantRecord(Base):
    __tablename__ = 'participant_record_tbl'
    participant_record_id = Column(Integer, primary_key=True)
    Event_name = Column(String(256))
    Date_attended = Column(Date)
    Hour = Column(String(256))
    Participant_id = Column(Integer)