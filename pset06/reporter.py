from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import *
from simulatetests import *

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

@app.route('/run/<int:run_num>')
def show_run(run_num):
    run_started = "No start time available... test run does not exist!"
    run_ended = "No end time available... test run does not exist!"
    for row in (select([runs.c.id, runs.c.started, runs.c.ended])
				.where(runs.c.id==run_num)
				.execute()):
        run_started = row["started"]
        run_ended = row["ended"]
    test_list = []
    for row in (select([tests.c.id, tests.c.name, tests.c.status])
				.where(tests.c.run==run_num)
				.execute()):
        test_list.append(row)
    return render_template('run.html', run_num=run_num, run_started=run_started, run_ended=run_ended, test_list=test_list)

@app.route('/run_test', methods = ['GET', 'POST'])
def run_test():
    if request.method == 'POST':
				new_run_num = 1 #default value in case there are no runs.
				for row in (select([runs.c.id, runs.c.started])
				.order_by(desc(runs.c.started))
				.limit(1)
				.execute()):
						new_run_num = int(row[0]) + 1
				fake_run_tests()
				return redirect(url_for('show_run', run_num=new_run_num))
    else:
        return "Please click the run button to use this function."

@app.route('/test/<test_name>')
def show_test(test_name):
    test_name = test_name.replace('%20', ' ') #May not be necessary
    run_list = []
    for row in (select([tests.c.id, tests.c.name, tests.c.status, tests.c.run, runs.c.ended])
				.where(and_(tests.c.name == str(test_name), tests.c.run == runs.c.id))
				.order_by(desc(runs.c.ended))
				.execute()):
        run_list.append(row)
    current_status = "Current Status: %s during run ending at %s." % (str(run_list[0]['status']), str(run_list[0]['ended']))
    previous_status = ""
    if run_list[0]['status'] == "PASS":
        search_for = "FAIL"
    elif run_list[0]['status'] == "FAIL":
        search_for = "PASS"
    else:
        search_for = None
    while previous_status == "" and search_for is not None:
        for row in run_list:
            if row['status'] == search_for:
                previous_status = "Last Change: %s during run ending at %s." % (str(row['status']), str(row['ended']))
                break
            if row == run_list[-1]:
                previous_status = "There is no record of this test having a different result."
    run_list = run_list[0:10]
    return render_template('test.html', test_name=test_name, run_list=run_list, current_status=current_status, previous_status=previous_status)
    

if __name__ == '__main__':
    app.debug = True
    app.run()
