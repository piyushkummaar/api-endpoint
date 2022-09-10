from pydantic import BaseModel
from datetime import  date


class PhonebookDB(BaseModel):
    first_name : str
    last_name : str
    rut_id : str
    phone_number : str
    qr_code_scanmevacuno : str
    created_datetime : date
    qr_code_registrocivil : str
    event_id : str

class EventDB(BaseModel):
    event_name : str
    event_location : str
    register_code : str
    export_code : str
    qr_code_scanmevacuno : str
    created_datetime : date
    qr_code_registrocivil : str

class getEventDB(BaseModel):
    event_id : int
    event_name : str
    event_location : str
    register_code : str
    export_code : str
    qr_code_scanmevacuno : str
    created_datetime : date
    qr_code_registrocivil : str

class ParticipantRecord(BaseModel):
    event_name : str
    date_attended : date
    hour : str
    participant_id : int

class Autosp(BaseModel):
    event_id : str
