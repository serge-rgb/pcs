from flask import Flask
from jinja2 import Template
from fileinput import close
from mimetypes import init
import soundcloud

USE_MIN = False
# USE_MIN = True

MIN_BLACKLIST = ['dan.js', 'dan.css']

IMG_EXTS = ['png', 'jpg']

def static(name):
    'foo.ext -> (foo.ext | foo.min.ext)'
    prelude = 'static/'
    strs = name.split('.')
    fname = strs[0]
    ext = strs[1]

    if USE_MIN and ext == 'js' or ext == 'css' and not (name in MIN_BLACKLIST):
        return prelude + fname + '.min.' + ext
    else:
        return prelude + name

    return 'NOPE'

application = Flask(__name__)
application.debug = True


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

albums = [
        Album('ep1',
            static('ep1.jpg'),
            [
                Track(client, 'https://soundcloud.com/dan_music/what-couldve-been-feat-zoya'),
                Track(client, 'https://soundcloud.com/dan_music/coyolxauhqui'),
                Track(client, 'https://soundcloud.com/dan_music/blue-dream'),
                Track(client, 'https://soundcloud.com/dan_music/93-n-feat-old-boy'),
                Track(client, 'https://soundcloud.com/dan_music/ladder'),
                Track(client, 'https://soundcloud.com/dan_music/your-way'),
                Track(client, 'https://soundcloud.com/dan_music/chirality-feat-mayssa-karaa'),
                ]),

        Album('ep2',
            static('ep2.jpg'),
            [
                Track(client, 'https://soundcloud.com/dan_music/another-dream'),
                Track(client, 'https://soundcloud.com/dan_music/the-lost-ark'),
                Track(client, 'https://soundcloud.com/dan_music/steps-of-creation'),
                Track(client, 'https://soundcloud.com/dan_music/for-all'),
                Track(client, 'https://soundcloud.com/dan_music/ratatrap'),
                Track(client, 'https://soundcloud.com/dan_music/northern-connection'),
                Track(client, 'https://soundcloud.com/dan_music/vii'),
                ]),

        Album('ep3',
            static('ep3.jpg'),
            [
                Track(client, 'https://soundcloud.com/dan_music/song-01'),
                Track(client, 'https://soundcloud.com/dan_music/let-the-music-come-in-feat'),
                Track(client, 'https://soundcloud.com/dan_music/lights-feat-gracie-jessop'),
                Track(client, 'https://soundcloud.com/dan_music/dance-in-the-universe-feat-dan'),
                Track(client, 'https://soundcloud.com/dan_music/hidden-memories'),
                Track(client, 'https://soundcloud.com/dan_music/tonight-feat-kristen-olsson'),
                ]),

        Album('ep4',
            static('ep4.jpg'),
            [

                Track(client, 'https://soundcloud.com/dan_music/killing-time'),
                Track(client, 'https://soundcloud.com/dan_music/oiee-oiee'),
                Track(client, 'https://soundcloud.com/dan_music/simmering-sun'),
                Track(client, 'https://soundcloud.com/dan_music/monday-suckz'),
                Track(client, 'https://soundcloud.com/dan_music/dafunk'),
                Track(client, 'https://soundcloud.com/dan_music/garde'),

                ]),
            ]

@application.route('/')
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
                        bootstrap_js_fname=static('bootstrap.js'),
                        bootstrap_css_fname=static('bootstrap.css'),
                        dan_css_fname=static('dan.css'),
                        dan_js_fname=static('dan.js'),
                        albums=albums,
                        dan_descr=gen_contact_html(dan_descr),
                        )
    return index_str


if __name__ == '__main__':
    dan_init()
#     application.debug = False
    application.run(host='0.0.0.0')
#     application.run()
