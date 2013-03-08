#!/usr/bin/env python

import random, time
import sqlalchemy
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy import select


db = MetaData()
db.bind = create_engine('sqlite:///data.sqlite')

runs = Table('runs', db,
             Column('id', Integer, primary_key=True),
             Column('started', DateTime),
             Column('ended', DateTime))


tests = Table('tests', db,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('status', String),
              Column('run', None, ForeignKey('runs.id')))


db.create_all()

# This file simulates a test run, which we'll then write a tool to analyze.

WORDS1 = ["checking", "making sure", "poking", "is", "ascertaining", ""]

WORDS2 = ["code", "network", "llama", "program", "main board", "laser",
          "blaster", "spline", "module", "archetecture", "computer",
          "screen", "system", "payment", "job", "fix", "duct tape"]

WORDS3 = ["halts", "works", "ok", "good", "satisfactory",
          "combobulated", "reticulated", "coherent", "meaningful",
          "useful", "green", "blue", "hot", "cold", "warmed up", ""]

class FakeTest(object):
    def __init__(self, name, probablility):
        self.name = name
        self.prob = probablility

    def __str__(self):
        return self.name

def generate_fake_tests():
    random.seed(12) #always give the same list
    tests = []
    for i in range(100):
        prob = random.random()
        if prob < 0.25: # weight the probability towards either success or failure.
            prob *= prob*prob
        else:
            prob = 1 - (1-prob)*(1-prob)*(1-prob)
        tests.append(FakeTest(" ".join([random.choice(WORDS1),
                                        random.choice(WORDS2),
                                        random.choice(WORDS3)]).strip(), prob))
    return tests


def report(run, name, success, pr=True):
    """Report on the success of a particular test in a particular run.
       Optionally print that report to the console"""
    dots = "."*(50-len(name))
    if success:
        success = "PASS"
    else:
        success = "FAIL"
    if pr:
        print name, dots, success
    # Along with printing (if pr is true), let the database know
    # what the test result was.

def start_run():
    """Start a test run.  Return the test run's ID"""

def end_run(id):
    """End the test run with the given id"""

def fake_run_tests(pr=True):
    tests = generate_fake_tests()
    random.seed()
    run = start_run()
    for test in tests:
        success = (random.random() < test.prob)
        time.sleep(random.random()/10)
        report(run, test.name, success, pr)
    end_run(run)


if __name__ == "__main__":
    fake_run_tests()
    for row in select([tests.c.name, tests.c.status]).execute():
        print row["name"], row["status"]
