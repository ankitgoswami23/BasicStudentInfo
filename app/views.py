from flask import render_template, request, redirect
from app.Models.Operations.StudentInfoModel import create_student, show_student_data, display_single_student, \
    edit_student, delete_student
from app import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        create_student(request.form)
        return redirect('/')
    else:
        return render_template('add_student.html')


@app.route('/show-student')
def show_student():
    header = ['First Name', 'Last Name', 'Standard', 'Phone Number', 'Address']
    student = show_student_data()
    return render_template('show_data.html', student=student, headers=header, head='Student Details')


@app.route('/edit-student/<stu_id>', methods=['GET', 'POST'])
def edit_student_data(stu_id):
    if request.method == 'POST':
        edit_student(stu_id, request.form)
        return redirect('/show-student')
    else:
        student = display_single_student(stu_id)
        return render_template('edit_student.html', data=student, head='Student Details')


@app.route('/delete-student/<stu_id>')
def delete_student_data(stu_id):
    delete_student(stu_id)

    return redirect('/show-student')
