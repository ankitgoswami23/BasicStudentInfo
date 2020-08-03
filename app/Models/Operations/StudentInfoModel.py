from app.Models.DatabaseModels.ModelStudentInfo import StudentInfo
from app import db


def create_student(data):
    try:
        obj_student = StudentInfo(first_name=data['first_name'],
                                  last_name=data['last_name'],
                                  address=data['address'],
                                  ph_no=data['ph_no'],
                                  standard=data['standard'])
        db.session.add(obj_student)
        db.session.commit()

    except Exception as e:
        print("Failed", e)

    return "Success"


def show_student_data():
    query = []
    stu_data = []
    try:
        query = db.session.query(StudentInfo.id,
                                 StudentInfo.first_name,
                                 StudentInfo.last_name,
                                 StudentInfo.standard,
                                 StudentInfo.ph_no,
                                 StudentInfo.address).all()
        if query is not None and query != []:
            for i in range(len(query)):
                stu_data.append(query[i]._asdict())

    except Exception as e:
        print('failed', e)

    return stu_data


def display_single_student(stu_id):
    query = []
    stu_data = {}
    try:
        query = db.session.query(StudentInfo.id,
                                 StudentInfo.first_name,
                                 StudentInfo.last_name,
                                 StudentInfo.standard,
                                 StudentInfo.ph_no,
                                 StudentInfo.address).filter(StudentInfo.id == stu_id).first()

        stu_data = query._asdict()
    except Exception as e:
        print('failed', e)

    return stu_data


def edit_student(stu_id, data):
    query = []
    stu_data = {}
    try:
        db.session.query(StudentInfo).filter(StudentInfo.id == stu_id).update(data)
        db.session.commit()

    except Exception as e:
        print('failed', e)

    return stu_data


def delete_student(stu_id):

    try:
        student = StudentInfo.query.get(stu_id)
        db.session.delete(student)
        db.session.commit()

    except Exception as e:
        print('failed', e)

    return "Success"