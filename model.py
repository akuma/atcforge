#coding=utf-8

import web
import uuid

db = web.database(dbn='sqlite', db='atcforge.db')

### Control CRUD
def get_controls():
    return db.select('at_control', order='modify_time DESC')

def get_control(id):
    try:
        return db.select('at_control', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_control(name, encoding, is_enable, description):
    id = uuid.uuid4().hex
    db.insert('at_control', id=id, name=name, encoding=encoding, is_enable=is_enable, description=description)

def update_control(id, name, encoding, is_enable, description):
    db.update('at_control', where="id=$id", vars=locals(), name=name, encoding=encoding, is_enable=is_enable, description=description)

def del_control(id):
    db.delete('at_control', where="id=$id", vars=locals())

### Action CRUD
def get_actions():
    return db.select('at_action', order='modify_time DESC')

def get_action(id):
    try:
        return db.select('at_action', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_action(name, is_enable, description):
    db.insert('at_action', name=name, is_enable=is_enable, description=description)

def update_action(id, name, is_enable, description):
    db.update('at_action', where="id=$id", vars=locals(), name=name, is_enable=is_enable, description=description)

def del_action(id):
    db.delete('at_action', where="id=$id", vars=locals())

### Control-Action CRUD
def get_control_actions(control_id):
    return db.select('at_control_action', where='control_id=$control_id', vars=locals())

def new_control_action(control_id, action_id, action_order):
    id = uuid.uuid4().hex
    db.insert('at_control_action', id=id, control_id=control_id, action_id=action_id, action_order=action_order)

def del_control_action(id):
	db.delete('at_control_action', where='id=$id', vars=locals())

### Function CRUD
def get_functions(action_id):
    return db.select('at_function', where='action_id=$action_id', order='modify_time DESC', vars=locals())

def get_function(id):
    try:
        return db.select('at_function', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_function(name, is_enable, description):
    id = uuid.uuid4().hex
    db.insert('at_function', id=id, name=name, is_enable=is_enable, description=description)

def update_function(id, name, is_enable, description):
    db.update('at_function', where="id=$id", vars=locals(), name=name, is_enable=is_enable, description=description)

def del_function(id):
    db.delete('at_function', where="id=$id", vars=locals())
