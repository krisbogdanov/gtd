from bottle import view, route, run, template

@route('/')
@view('index')
def index():
    return template('index')

run(host='localhost', port=8080)