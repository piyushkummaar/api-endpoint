from fastapi import FastAPI, Body, Depends
from fastapi.encoders import jsonable_encoder
import schemas
from fastapi.responses import ORJSONResponse
import models
import uvicorn
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 
from datetime import date


Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI(
    title="API ENDPOINT's",
    description="API build in Python.",
    version="1.0.0",
)


@app.get("/",tags=['Documentation'],response_class=ORJSONResponse)
def documentation_urls(session: Session = Depends(get_session)):
    res = {
        "doc_url":"https://api-endpointss.herokuapp.com/docs",
        "re_doc_url":"https://api-endpointss.herokuapp.com/redoc"
    }
    
    return ORJSONResponse(res)

@app.post("/automationscrape",tags=['Automation Scraper'])
def autoamtion_scraper(event:schemas.Autosp,session: Session = Depends(get_session)):
    '''
    This script enable the python script to run the selenium automation script that.
    Pull out the data from the website. From Given QR.
    '''
    print(event.event_id)
    # # automation
    # from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options
    # from selenium.webdriver.chrome.service import Service as ChromeService
    # from webdriver_manager.chrome import ChromeDriverManager
    # from selenium.webdriver.common.by import By
    # import time
    # opt = Options()
    # opt.add_argument("--disable-infobars")
    # opt.add_argument("start-maximized")
    # opt.add_argument("--headless")
    # opt.add_argument("--disable-dev-shm-usage")
    # opt.add_argument("--no-sandbox")
    # opt.add_argument("--disable-extensions")
    # # Pass the argument 1 to allow and 2 to block
    # opt.add_experimental_option("prefs", { \
    #     "profile.default_content_setting_values.media_stream_camera": 1,
    #     })
    # _url_path = "https://scanmevacuno.gob.cl/"
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=opt,)
    # driver.get(_url_path)
    # time.sleep(3)
    # driver.find_element(By.CLASS_NAME,'color-purple').click()
    # driver.find_element(By.CLASS_NAME,'dialog-button-bold').click()
    # time.sleep(10)
    # data = driver.find_element(By.CLASS_NAME,'identidad')
    # driver.close()
    # # end
    # res = data.text.split('\n')
    # event = models.EventDB(
    #     event_name = res[0],
    #     event_location = res[1],
    #     register_code = res[2],
    #     export_code = ' ',
    #     qr_code_scanmevacuno = ' ',
    #     created_datetime = date.today(),
    #     qr_code_registrocivil = ' ',
    # )
    # data = 
    # return {"data":data.text.split('\n')}
    return event.event_id
    
@app.get("/getevents",tags=['Events'])
def get_events(session: Session = Depends(get_session)):
    events = session.query(models.EventDB).all()
    return events

@app.get("/getevent/{id}",tags=['Events'])
def get_event(id:int, session: Session = Depends(get_session)):
    event = session.query(models.EventDB).get(id)
    return event


@app.post("/addevent",tags=['Events'])
def add_event(event:schemas.EventDB, session: Session = Depends(get_session)):
    '''
    This endpoint add the infomation to the Event table.
    event_id with inserted automatically.
    '''
    event = models.EventDB(
        event_name = event.event_name,
        event_location = event.event_location,
        register_code = event.register_code,
        export_code = event.export_code,
        qr_code_scanmevacuno = event.qr_code_scanmevacuno,
        created_datetime = event.created_datetime,
        qr_code_registrocivil = event.qr_code_registrocivil,
    )
    session.add(event)
    session.commit()
    session.refresh(event)

    return event


@app.put("/updateevent/{id}",tags=['Events'])
def update_event(id:int, event:schemas.EventDB, session: Session = Depends(get_session)):
    eventObject = session.query(models.EventDB).get(id)
    eventObject.event_name = event.event_name
    eventObject.event_location = event.event_location
    eventObject.register_code = event.register_code
    eventObject.export_code = event.export_code
    eventObject.qr_code_scanmevacuno = event.qr_code_scanmevacuno
    eventObject.created_datetime = event.created_datetime
    eventObject.qr_code_registrocivil = event.qr_code_registrocivil
    session.commit()
    return eventObject


@app.delete("/deleteevent/{id}",tags=['Events'])
def delete_event(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.EventDB).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Event was deleted...'

#   ==================== PHONEBOOK ====================
@app.get("/getphonebooks",tags=['Phonebook'])
def list_of_phonebook(session: Session = Depends(get_session)):
    events = session.query(models.PhonebookDB).all()
    return events

@app.get("/getphonebook/{id}",tags=['Phonebook'])
def get_phonebook(id:int, session: Session = Depends(get_session)):
    event = session.query(models.PhonebookDB).get(id)
    return event


@app.post("/addphonebook",tags=['Phonebook'])
def add_phonebook(item:schemas.PhonebookDB, session: Session = Depends(get_session)):
    '''
    This endpoint add the infomation to the phonebook table.
    participant_id with inserted automatically.
    '''
    item = models.PhonebookDB(
        first_name = item.first_name,
        last_name = item.last_name,
        rut_id = item.rut_id,
        phone_number = item.phone_number,
        qr_code_scanmevacuno = item.qr_code_scanmevacuno,
        created_datetime = item.created_datetime,
        qr_code_registrocivil = item.qr_code_registrocivil,
    )
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.put("/updatephonebook/{id}",tags=['Phonebook'])
def update_phonebook(id:int, item:schemas.PhonebookDB, session: Session = Depends(get_session)):
    itemObject = session.query(models.PhonebookDB).get(id)
    itemObject.first_name = item.first_name
    itemObject.last_name = item.last_name
    itemObject.rut_id = item.rut_id
    itemObject.phone_number = item.phone_number
    itemObject.qr_code_scanmevacuno = item.qr_code_scanmevacuno
    itemObject.created_datetime = item.created_datetime
    itemObject.qr_code_registrocivil = item.qr_code_registrocivil
    session.commit()
    return itemObject


@app.delete("/deletephonebook/{id}",tags=['Phonebook'])
def delete_phonebook(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.PhonebookDB).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Phonebook was deleted...'

#   ==================== ParticipantRecord ====================
@app.get("/getparticipantrecord",tags=['Participant Record\'s'])
def list_of_participant_records(session: Session = Depends(get_session)):
    events = session.query(models.ParticipantRecord).all()
    return events

@app.get("/getparticipantrecord/{id}",tags=['Participant Record\'s'])
def get_participant_record(id:int, session: Session = Depends(get_session)):
    event = session.query(models.ParticipantRecord).get(id)
    return event


@app.post("/addparticipantrecord",tags=['Participant Record\'s'])
def add_participant_record(item:schemas.ParticipantRecord, session: Session = Depends(get_session)):
    '''
    This endpoint add the infomation to the phonebook table.
    participant_id with inserted automatically.
    '''
    item = models.ParticipantRecord(
        event_name = item.event_name,
        date_attended = item.date_attended,
        hour = item.hour,
        participant_id = item.participant_id,
    )
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.put("/updateparticipantrecord/{id}",tags=['Participant Record\'s'])
def update_participant_record(id:int, item:schemas.ParticipantRecord, session: Session = Depends(get_session)):
    itemObject = session.query(models.ParticipantRecord).get(id)
    itemObject.event_name = item.event_name
    itemObject.date_attended = item.date_attended
    itemObject.hour = item.hour
    itemObject.participant_id = item.participant_id
    session.commit()
    return itemObject


@app.delete("/deleteparticipantrecord/{id}",tags=['Participant Record\'s'])
def delete_participant_record(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.ParticipantRecord).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Phonebook was deleted...'



if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True,reload=True)