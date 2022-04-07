from marshmallow import fields, Schema
from . import db


class passengerModel(db.Model):
    __tablename__ = 'passengers'

    id = db.Column(db.Integer, primary_key=True)
    survived = db.Column(db.Integer)
    pclass = db.Column(db.Integer)
    name = db.Column(db.String(255))
    sex = db.Column(db.String(6))
    age = db.Column(db.Float)
    siblings_spouses_aboard = db.Column(db.Integer)
    parents_children_aboard = db.Column(db.Integer)
    fare = db.Column(db.Float)

    def __init__(self, data):
        self.survived = data.get('survived')
        self.pclass = data.get('pclass')
        self.name = data.get('name')
        self.sex = data.get('sex')
        self.age = data.get('age')
        self.siblings_spouses_aboard = data.get('siblings_spouses_aboard')
        self.parents_children_aboard = data.get('parents_children_aboard')
        self.fare = data.get('fare')

    # save passenger to db
    def save(self):
        db.session.add(self)
        db.session.commit()

    # update passenger in db
    def update(self, data):
        for key, item in data.items():
          setattr(self, key, item)
        db.session.commit()

    # delete passenger from db
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # retrieves all passengers from db
    @staticmethod
    def get_all_passengers():
        return passengerModel.query.all()

    # retrieves passenger from db by his id
    @staticmethod
    def get_passenger(id):
        return passengerModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class passengerSchema(Schema):
    id = fields.Int(dump_only=True)
    survived = fields.Int(required=True)
    pclass = fields.Int(required=True)
    name = fields.String(required=True)
    sex = fields.String(required=True)
    age = fields.Int(required=True)
    siblings_spouses_aboard = fields.Int(required=True)
    parents_children_aboard = fields.Int(required=True)
    fare = fields.Float(required=True)
