from flask import *
from sqlalchemy import *
from datetime import datetime

app = Flask(__name__)

db = MetaData()
db.bind = create_engine('sqlite:///data.sqlite')

students = Table('students', db,
        Column('id', Integer, primary_key=True),
        Column('district_id', String),
        Column('first_name', String),
        Column('last_name', String),
        Column('time_added', DATETIME),
        Column('program_id', None, ForeignKey('programs.id')),
        Column('enroll_status', String),
        Column('QR_URL', String)) #URL the QR code will route to
        #Ideally, I'd like to add a column adding a QR code image...

programs = Table('programs', db,
		Column('id', Integer, primary_key=True),
		Column('program_name', String),
	    Column('time_added', DATETIME))

db.create_all()

#The following method adds a student to the database. This is done
#with a method because eventually I want to generate and insert the
#student's QR code here.

def add_student(district_id, first_name, last_name, program_id):
  #First figure out the ID of the student to be added for use in URL generation.
  #Afterwards, insert the student record (complete with .execute())
  new_student_id = 1 #default value in case there are no students in the database.
  get_most_recent = select([students.c.id]).order_by(desc(students.c.time_added)).limit(1)
  for row in get_most_recent.execute():
    new_student_id = int(row[0]) + 1
  if len(select([students.c.id]).where(students.c.id==new_student_id) == 0:
	ins = students.insert().values(district_id=district_id, first_name=first_name, last_name=last_name, time_added=datetime.now(), program_id=program_id, QR_URL=url_for('check_in',  new_student_id))
	ins.execute()

#For the first run, I am generating a test program and student here.
new_program = programs.insert().values(program_name="ExCEL", time_added=datetime.now())
new_program.execute()
add_student('H0101010101010', "Missus", "Testie", 1)

@app.route('/show_students/<program_id>')
def show_students(program_id):
  disp_list = [] #list of entries to display on the webpage, grouped by program_name
  for row in (select([students.c.id, students.c.district_id, students.c.first_name, students.c.last_name, students.c.time_added, students.c.enroll_status, students.c.QR_URL])
          .where(students.c.program_id==program_id)
          .execute()):
  disp_list.append(row)
    program_name = "'Not in System'" #default value if the program_id is not in database
  for row in (select([programs.c.program_name]).where(programs.c.id==program_id)):
    program_name = 
  return render_template('show_students.html', program_name=program_name, disp_list=disp_list)

@app.route('/check_in/<int:student_id>', methods = ['GET', 'POST'])
def check_in(student_id):
  #Prompts user to choose the method of checking in once the code has been scanned.
  if request.method == 'POST':
    pass
  else:
    return render_template('check_in.html', student_id=student_id)

