from flask import Flask, render_template, session, redirect,url_for
app = Flask(__name__)
app.secret_key = 'counter_key'

@app.route('/', methods=['GET'])
def count():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html', visits=session['visits'])



@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increase_visit_count')
def increase_visit_count():
    session['visits'] += 1
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)