from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import *
from atm_test import *

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
	
if __name__ == '__main__':
  app.debug = True
  app.run()
