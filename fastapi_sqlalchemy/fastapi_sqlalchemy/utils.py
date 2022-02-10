from database import SessionLocal
import models
from models import Student_model
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def database_retrive(db):
    user_data = db.query(models.Student_model).filter(Student_model.id >= 14)
    response = {}
    out_res = []
    for each in user_data:
        response['name'] = each.name
        response['Telugu'] = each.Telugu
        response['English'] = each.English
        response['Hindi'] = each.Hindi
        response['Science'] = each.Science
        response['Maths'] = each.Maths
        response['Biology'] = each.Biology
        response['status'] = each.status
        response['chance'] = each.chance

        out_res.append(response)
    return out_res

def database_retrive_one(id,db):
    user_data = db.query(Student_model).filter(Student_model.stu_id == id).first()
    response = {}
    response['name'] = user_data.name
    response['Telugu'] = user_data.Telugu
    response['English'] = user_data.English
    response['Hindi'] = user_data.Hindi
    response['Science'] = user_data.Science
    response['Maths'] = user_data.Maths
    response['Biology'] = user_data.Biology
    response['status'] = user_data.status
    response['chance'] = user_data.chance

    return response

def database_update(name,Telugu,English,Hindi,Science, Maths,Biology,status,chance,db):
    update_obj = db.query(Student_model).filter(Student_model.eid == id).first()
    update_obj.name = name
    update_obj.Telugu = Telugu
    update_obj.English = English
    update_obj.Hindi = Hindi
    update_obj.Science = Science
    update_obj.Maths = Maths
    update_obj.Biology = Biology
    update_obj.status = status
    update_obj.chance = chance

    db.add(update_obj)
    db.commit()
    db.refresh(update_obj)
    return "data updated successfully"

def database_delete(id,db):
    if db.query(Student_model).filter(Student_model.id == id).delete():
        db.commit()
        return "success"
    else:
        return 'user not found'