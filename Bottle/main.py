# bottle is a single file backend engine

from bottle import route, run

@route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    run(host='localhost', port=3333, debug=False)
