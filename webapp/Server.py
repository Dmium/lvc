from bottle import route, run
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('.'),
)

@route('/')
def index():
    template = env.get_template("index.html")
    return template.render()

if __name__ == "__main__":
    run(host='localhost', port=8080)
