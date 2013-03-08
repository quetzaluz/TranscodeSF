from flask import Flask, render_template

app = Flask(__name__)


@app.route('/run/<run>')
def show_run(run):
    return render_template('run.html', run=run)


if __name__ == '__main__':
    app.run()
