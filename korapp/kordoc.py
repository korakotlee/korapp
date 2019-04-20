import os
from flask import Flask
# from flask import send_from_directory
import flask
import markdown2
# import pkg_resources
import pkgutil
from korapp import html_template

app = Flask(__name__)


@app.route('/img/<filename>')
def img(filename):
    cwd = os.getcwd()
    return flask.send_file(cwd+'/img/'+filename, as_attachment=True)


@app.route("/")
def hello():
    # resource_package = __name__  # Could be any module/package name
    # resource_path = '/'.join('water.css')  # Do not use os.path.join()
    # css = pkg_resources.resource_string(resource_package, resource_path)
    css = pkgutil.get_data(__package__, 'water.css')
    css = str(css, 'utf-8')
    cwd = os.getcwd()
    out = html_template.outline
    out = out.replace('[title]', f'Brain {cwd}')
    out = out.replace('[css]', css)
    # out = out.replace('[css]', flask.url_for('static', filename='water.css'))

    files = [os.path.join("gen", file) for file in os.listdir("gen")]
    print(files)
    body = markdown2.markdown_path('README.md')
    body += markdown2.markdown_path('new.md')
    for f in files:
        if f.endswith('.md'):
            body += markdown2.markdown_path(f)
    out = out.replace('[body]', body)
    return out


def init():
    app.run(host='127.0.0.1', port=8000, debug=True)