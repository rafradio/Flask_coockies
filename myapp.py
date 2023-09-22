from flask import Flask, request, make_response, url_for
from flask import render_template, redirect, session
from markupsafe import escape
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.get('/')
def index_get():
    name = request.cookies.get('username')
    print(f'Hello {name}!')
    return render_template('index.html')

@app.post('/')
def index_post():
    session['email'] = request.form.get('email') or 'NoEmail'
    response = make_response(redirect(url_for('hello')))
    name = escape(request.form.get('name'))
    # email = request.form.get('email')
    response.set_cookie('username', name)
    # response.set_cookie('email', email)
    print(f'Hello {name}!')
    return response

@app.route('/hello') 
def hello():
    name = request.cookies.get('username')
    email = session['email']
    print(f'Again {name}!')
    print(session)
    print(f'My email {email}!')
    data = {'name': name}
    return render_template('hello.html', **data)

@app.route('/deleteCoockie') 
def cockDel():
    response = make_response(redirect(url_for('index_get')))
    response.delete_cookie('username')
    session.pop('email', None)
    print(session)
    return response

if __name__ == '__main__': 
    app.run(debug=True)