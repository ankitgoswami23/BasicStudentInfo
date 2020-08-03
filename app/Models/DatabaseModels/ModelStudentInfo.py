from app import db


class StudentInfo(db.Model):
    __tablename__ = 'studentinfo'

    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column('first_name', db.String(45))
    last_name = db.Column('last_name', db.String(45))
    address = db.Column('address', db.String(100))
    ph_no = db.Column('ph_no', db.String(12))
    standard = db.Column('standard', db.String(3))

    def __init__(self, first_name, last_name, address, ph_no, standard):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.ph_no = ph_no
        self.standard = standard

    def __repr__(self):
        data = {'first_name': self.first_name,
                'last_name': self.last_name,
                'address': self.address,
                'ph_no': self.ph_no,
                'standard': self.standard}

        return data
