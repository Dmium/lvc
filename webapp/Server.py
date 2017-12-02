from bottle import route, run, static_file, request
from jinja2 import Environment, FileSystemLoader
from Node import Node
import time

env = Environment(
    loader=FileSystemLoader('.'),
)

@route('/')
def index():
    template = env.get_template("index.html")

    test_node = Node("test", "test", time.time())
    nodes = [test_node]

    return template.render(dir_nodes=nodes)

@route('/css/styles.css')
def styles():
    return static_file('styles.css', '.')

@route('/js/lvc.min.js')
def js():
    return static_file('lvc.min.js', '.')

@route('/revisions/<fp>')
def revisions(fp):
    template = env.get_template("revisions.html")
    return template.render(filepath=fp)

@route('/api/getRevisions')
def get_revisions():
    return "[{\"timestamp\": 1512218675, \"content\":\"bla bla bla\"}]"

@route('/api/addFile', method='POST')
def add_file():
    filename = request.forms.get('filename')
    print(filename)
    return 'success'

if __name__ == "__main__":
    run(host='localhost', port=8080)
