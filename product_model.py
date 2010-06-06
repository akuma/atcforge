#coding=utf-8

#import model
from model import db

### Product CRUD
def get_products():
    return db.select('at_product', order='creation_time DESC')

def get_product(id):
    try:
        return db.select('at_product', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_product(ename, cname, description):
    id = model.guid()
    db.insert('at_product', id=id, ename=ename, cname=cname, description=description)

def update_product(id, ename, cname, description):
    db.update('at_product', where="id=$id", vars=locals(), ename=ename, cname=cname, description=description)

def del_product(id):
    db.delete('at_product', where="id=$id", vars=locals())
