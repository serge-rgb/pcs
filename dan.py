from flask import Flask
from jinja2 import Template
from fileinput import close
from mimetypes import init

USE_MIN = False
# USE_MIN = True


def static(name):
    'foo.ext -> (foo.ext | foo.min.ext)'
    prelude = 'static/'
    if not USE_MIN:
        return prelude + name
    strs = name.split('.')
    fname = strs[0]
    ext = strs[1]
    return prelude + fname + '.min.' + ext


app = Flask(__name__)
app.debug = True


class Album(object):
    def __init__(self, img, text):
        self.img = img
        self.text = text

@app.route('/')
def hello_world():
    dan_file = open('templates/dan.html')
    dan_src = dan_file.read()
    dan_file.close()
    tmpl = Template(dan_src)
    index_str = tmpl.render(name='Daniel',
                        bootstrap_js_fname=static('js/bootstrap.js'),
                        bootstrap_css_fname=static('css/bootstrap.css'),
                        dan_css_fname=static('css/dan.css'),
                        albums=[Album(static('img/Placeholder.png'), 'foo') for _ in xrange(4)],
                        album_1=static('img/Placeholder.png'))
    return index_str


if __name__ == '__main__':
#     app.debug = False
#     app.run(host='0.0.0.0')
    app.run()
