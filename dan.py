from flask import Flask
from jinja2 import Template
from fileinput import close
from mimetypes import init

USE_MIN = False
USE_MIN = True

MIN_BLACKLIST = ['js/dan.js', 'css/dan.css']

def static(name):
    'foo.ext -> (foo.ext | foo.min.ext)'
    prelude = 'static/'
    strs = name.split('.')
    fname = strs[0]
    ext = strs[1]

    if not USE_MIN or ext == "png" or name in MIN_BLACKLIST:
        return prelude + name

    if USE_MIN and ext == 'js' or ext == 'css' and not (name in MIN_BLACKLIST):
        return prelude + fname + '.min.' + ext

    return "NOPE"


app = Flask(__name__)
app.debug = True


class Album(object):
    def __init__(self, img, text, tracks):
        self.img = img
        self.text = text
        self.tracks = tracks


@app.route('/')
def hello_world():
    dan_file = open('templates/dan.html')
    dan_src = dan_file.read()
    dan_file.close()
    tmpl = Template(dan_src)
    albums = [Album(static('img/Placeholder.png'),
                    'foo',
                    ['https://soundcloud.com/dan_music/last-time'])]
    index_str = tmpl.render(name='Daniel',
                        bootstrap_js_fname=static('js/bootstrap.js'),
                        bootstrap_css_fname=static('css/bootstrap.css'),
                        dan_css_fname=static('css/dan.css'),
                        dan_js_fname=static('js/dan.js'),
                        albums=albums,
                        )
    return index_str


if __name__ == '__main__':
#     app.debug = False
    app.run(host='0.0.0.0')
#     app.run()
