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
    for row in select([runs.c.id, runs.c.started, runs.c.ended]).where(runs.c.id==run_num).execute():
        run_started = row["started"]
        run_ended = row["ended"]
    testlist = []
    for row in select([tests.c.id, tests.c.name, tests.c.status]).where(tests.c.run==run_num).execute():
        testlist.append([row[0], row[1], row[2]])
    return render_template('run.html', run_num=run_num, run_started=run_started, run_ended=run_ended, testlist=testlist)


if __name__ == '__main__':
    app.run()
