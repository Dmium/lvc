from bottle import route, run, static_file, request
from jinja2 import Environment, FileSystemLoader
from webapp.Node import Node
import time
from WebWrapper import WebWrapper

env = Environment(
    loader=FileSystemLoader('./webapp/'),
)

@route('/')
def index():
    template = env.get_template("index.html")
    print(WebWrapper().get_paths_list())
    test_node = Node("test", "test", time.time())
    nodes = [test_node]

    return template.render(dir_nodes=nodes)

@route('/css/styles.css')
def styles():
    return static_file('styles.css', './webapp/')

@route('/js/lvc.min.js')
def js():
    return static_file('lvc.min.js', './webapp/')

@route('/revisions/<fp>')
def revisions(fp):
    template = env.get_template("revisions.html")
    return template.render(filepath=fp)

@route('/api/getRevisions/<fp>')
def get_revisions(fp):
    return WebWrapper().get_commits_for_path(fp)

@route('/api/addFile', method='POST')
def add_file():
    filename = request.forms.get('filename')
    print(filename)
    return 'success'

@route('/api/getFileList')
def get_file_list():
    return WebWrapper().get_paths_list_json()

def start():
    run(host='localhost', port=8080)
