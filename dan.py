from flask import Flask
from jinja2 import Template
from fileinput import close
from mimetypes import init
import soundcloud

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

    return 'NOPE'

app = Flask(__name__)
app.debug = True


class Track(object):
    def __init__(self, client, url):
        self.url = url
        self.sc = client.get('/resolve', url=url)


class Album(object):
    def __init__(self, title, img, tracks):
        self.title = title
        self.img = img
        self.tracks = tracks


def dan_init():
    pass

################################################################################
client = soundcloud.Client(client_id="feadf530fe2b6e545774f60b12b24cf2")

dan_descr = '''
Daniel Gonzalez
dgonzalez@berklee.edu
'''

albums = [Album('foo',
                static('img/Placeholder.png'),
                [Track(client,
                       'https://soundcloud.com/dan_music/last-time')]),
          Album('bar',
                static('img/Placeholder.png'),
                [Track(client,
                       'https://soundcloud.com/dan_music/google-plex-v-hope'),
                 Track(client,
                       'https://soundcloud.com/dan_music/googleplex-iv-home'),
                 ]),
          ]


@app.route('/')
def dan_main():
    def gen_contact_html(dan_descr):
        lines = dan_descr.split('\n');
        html = ''
        for line in lines:
            if len(line) <= 1:
                continue
            html += line + "<br>"
        return html

    dan_file = open('templates/dan.html')
    dan_src = dan_file.read()
    dan_file.close()
    tmpl = Template(dan_src)
    index_str = tmpl.render(name='Daniel',
                        bootstrap_js_fname=static('js/bootstrap.js'),
                        bootstrap_css_fname=static('css/bootstrap.css'),
                        dan_css_fname=static('css/dan.css'),
                        dan_js_fname=static('js/dan.js'),
                        albums=albums,
                        dan_descr=gen_contact_html(dan_descr),
                        )
    return index_str


if __name__ == '__main__':
    dan_init()
#     app.debug = False
    app.run(host='0.0.0.0')
#     app.run()
