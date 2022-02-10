from fastapi import FastAPI, Depends
import uvicorn
from schemas import Student
from sqlalchemy.orm import Session
from utils import get_db
from service import service_insert, service_retrive, \
    service_retrive_one, service_update,service_delete
import models
from database import engine
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

@app.post('/insert',status_code=201 )
def insert_data(emp : Student, db : Session = Depends(get_db)):
    total = emp.Telugu + emp.English + emp.Hindi + emp.Science + emp.Maths + emp.Biology
    average = (total / 6)
    print(average)
    status=''
    if average > 90:
       status = 'distiction'
    elif average > 75 and average < 90:
        status = 'average'
    elif average < 75:
        status = 'fail'

    print(status)
    if status == 'fail':
        chance = 'yes'
    else:
        chance = 'no'
    new_user = models.Student_model(name = emp.name,Telugu=emp.Telugu,English=emp.English,
                                    Hindi=emp.Hindi,Science=emp.Science,Maths=emp.Maths,Biology=emp.Biology,status=status,chance=chance)

    return service_insert(new_user,db)

@app.get('/retrieve',status_code=200)
def retrieve_data(db : Session = Depends(get_db)):
    return service_retrive(db)

@app.get('/retrieve/{id}',status_code=200)
def retrieve_data(id:int, db : Session = Depends(get_db)):
    return service_retrive_one(id,db)

@app.put('/update')
def update_data(emp : Student, db : Session = Depends(get_db)):

    total = emp.Telugu + emp.English + emp.Hindi + emp.Science + emp.Maths + emp.Biology
    average = (total / 6)
    print(average)
    if average > 90:
       status = 'distiction'
    elif average > 75 and average < 90:
        status = 'average'
    elif average < 75:
        status = 'fail'

    if status == 'fail':
        chance = 'yes'
    else:
        chance = 'no'
    id = emp.id
    name = emp.name
    Telugu = emp.Telugu
    English = emp.English
    Hindi = emp.Hindi
    Science = emp.Science
    Maths = emp.Maths
    Biology = emp.Biology
    status = status
    chance = chance
    return service_update(name,Telugu,English,Hindi,Science, Maths,Biology,status,chance,db)

@app.delete('/delete/{id}')
def delete_data(id:int,db : Session = Depends(get_db)):
    return service_delete(id,db)


if __name__ == '__main__':
    uvicorn.run(app)