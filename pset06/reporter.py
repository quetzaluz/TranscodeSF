from flask import Flask, render_template
from sqlalchemy import *

app = Flask(__name__)

db = MetaData()
db.bind = create_engine('sqlite:///data.sqlite')

runs = Table('runs', db,
             Column('id', Integer, primary_key=True),
             Column('started', DATETIME),
             Column('ended', DATETIME))

tests = Table('tests', db,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('status', String),
              Column('run', None, ForeignKey('runs.id')))


db.create_all()

@app.route('/run/<run_num>')
def show_run(run_num):
    run_started = "No start time available... test run does not exist!"
    run_ended = "No end time available... test run does not exist!"
    for row in select([runs.c.id, runs.c.started, runs.c.ended]).where(runs.c.id==run_num).execute():
        run_started = row["started"]
        run_ended = row["ended"]
    test_list = []
    for row in select([tests.c.id, tests.c.name, tests.c.status]).where(tests.c.run==run_num).execute():
        test_list.append([row[0], row[1], row[2]])
    return render_template('run.html', run_num=run_num, run_started=run_started, run_ended=run_ended, test_list=test_list)

@app.route('/test/<test_name>')
def show_test(test_name):
    test_name = test_name.replace('%20', ' ') #May not be necessary
    run_list = []
    for row in select([tests.c.id, tests.c.name, tests.c.status, tests.c.run, runs.c.ended]).where(and_(tests.c.name == str(test_name), tests.c.run == runs.c.id)).order_by(runs.c.ended).limit(10).execute():
        run_list.append([row[0], row[1], row[2], row[3], row[4]])
    current_status = ""    
    previous_status = ""
##Going to code to make this loop run for both FAIL and PASS in two iterations.
##But for now, this works.
    if run_list[0][2] == "PASS":
        current_status = "Current Status: PASS during run ending at %s." % str(run_list[0][4])
        for run in run_list:
            if run[2] == "FAIL":
                previous_satus = "Changed From:   FAIL during run ending at %s." % str(run[4])
            elif run[2] != "FAIL": 
                previous_status = "Changed From:   There is no record of a FAIL result for this test."
    elif run_list[0][2] == "FAIL":
        current_status = "Current Status: FAIL during test run ending at %s." % str(run_list[0][4])
        for run in run_list:
            if run[2] == "PASS":
                previous_status = "Changed From:   PASS during test run ending at %s. " % str(run[4])
            elif run[2] != "PASS": 
                previous_status = "Changed From:   There is no record of a PASS result for this test."
    return render_template('test.html', test_name=test_name, run_list=run_list, current_status=current_status, previous_status=previous_status)
        

if __name__ == '__main__':
    app.debug = True
    app.run()
