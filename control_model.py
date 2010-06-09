#coding=utf-8

import model
from model import db

### Control CRUD
def get_controls():
    return db.select('at_control', order='modify_time DESC')

def get_control(id):
    try:
        return db.select('at_control', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_control(product_id, name, is_enable, description):
    id = model.guid()
    db.insert('at_control', id=id, product_id=product_id, name=name, encoding='GBK', is_enable=is_enable, description=description)

def update_control(id, name, is_enable, description):
    db.update('at_control', where="id=$id", vars=locals(), name=name, is_enable=is_enable, description=description)

def del_control(id):
    db.delete('at_control', where="id=$id", vars=locals())

### Control-Action CRUD
def get_control_actions(control_id):
    return db.select('at_control_action', where='control_id=$control_id', vars=locals())

def new_control_action(control_id, action_id, action_order):
    id = uuid.uuid4().hex
    db.insert('at_control_action', id=id, control_id=control_id, action_id=action_id, action_order=action_order)

def del_control_action(id):
	db.delete('at_control_action', where='id=$id', vars=locals())
