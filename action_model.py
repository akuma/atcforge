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

def get_action_of_control(control_id):
    return db.query('SELECT a.id, a.serial, a.name, a.state, a.description, a.modify_time, r.is_enable \
                     FROM at_action a, at_action_ref r \
                     WHERE a.id = r.action_id AND r.control_id = $control_id \
                     ORDER BY r.action_order', vars={'control_id': control_id})

def serial_exists(product_id, serial, action_id=None):
    if action_id:
        result = db.select('at_action', what='serial', where='product_id=$product_id AND serial=$serial AND id<>$action_id', vars=locals())
    else:
        result = db.select('at_action', what='serial', where='product_id=$product_id AND serial=$serial', vars=locals())

    if result:
        return True
    else:
        return False

def new_action(product_id, serial, name, state, description):
    id = model.guid()
    db.insert('at_action', id=id, product_id=product_id, serial=serial, name=name, state=state, description=description)

def update_action(id, serial, name, state, description):
    db.update('at_action', where='id=$id', vars=locals(), serial=serial, name=name, state=state, description=description)
