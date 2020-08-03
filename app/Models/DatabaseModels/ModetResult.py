from config import app, db


class Result(db.Model):
    __tablename__ = 'Result'

    result_id = db.Column('result_id', db.Integer, autoincrement=True, primary_key=True)
    student_id = db.Column('student_id', db.ForeignKey('StudentInfo.id'))
    standard = db.Column('exam_season', db.String(3))
    marks = db.Column('marks', db.String(3))
    total_marks = db.Column('total_marks', db.String(3))
    obtained_marks = db.Column('obtained', db.String(3))

    def __init__(self, student_id, standard, marks, total_marks, obtained_marks):
        self.student_id = student_id
        self.standard = standard
        self.marks = marks
        self.total_marks = total_marks
        self.obtained_marks = obtained_marks

    def __repr__(self):
        data = {'student_id': self.student_id,
                'standard': self.standard,
                'marks': self.marks,
                'total_marks': self.total_marks,
                'obtained_marks': self.obtained_marks}

        return data
