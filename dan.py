from flask import Flask
from jinja2 import Template

dan_file = open('templates/dan.html')
dan_src = dan_file.read()
tmpl = Template(dan_src)
index_str = tmpl.render(name='Daniel')

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return index_str

if __name__ == '__main__':
    app.run()
