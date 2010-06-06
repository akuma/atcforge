#coding=utf-8

import model
from model import db

### Action CRUD
def get_actions(product_id):
    if product_id == None:
        return []
    else:
        return db.select('at_action', where='product_id=$product_id', order='modify_time DESC', vars=locals())

def get_action(id):
    try:
        return db.select('at_action', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def serial_exists(product_id, serial):
    serial = db.select('at_action', what='serial', where='product_id=$product_id AND serial=$serial', vars=locals())
    if serial:
        return True
    else:
        return False

def new_action(product_id, serial, name, state, description):
    id = model.guid()
    db.insert('at_action', id=id, product_id=product_id, serial=serial, name=name, state=state, description=description)

def update_action(id, serial, name, state, description):
    db.update('at_action', where='id=$id', vars=locals(), serial=serial, name=name, state=state, description=description)
