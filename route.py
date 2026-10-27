from bottle import Bottle, run, static_file, request, response, redirect
from app.controllers.application import Application

app = Bottle()
ctl = Application()

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/')
@app.route('/helper')
def helper():
    return ctl.render('helper')

@app.route('/portal', method='GET')
def login():
    return ctl.render('portal')

@app.route('/portal', method='POST')
def action_portal():
    username = request.forms.get('username')
    password = request.forms.get('password')
    session_id, username = ctl.authenticate_user(username, password)
    if session_id:
        response.set_cookie('session_id', session_id, httponly=True, max_age=3600)
        redirect('/dashboard')
    else:
        redirect('/portal')

@app.route('/dashboard', method='GET')
def dashboard():
    return ctl.render('dashboard')

@app.route('/logout', method='POST')
def logout():
    ctl.logout_user()
    response.delete_cookie('session_id')
    redirect('/helper')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)