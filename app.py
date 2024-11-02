# pip install Flask-Babel
# pip install Flask
#  pybabel.exe extract -F babel.cfg -o messages.pot .
# pybabel.exe init -i .\messages.pot -d translations -l es
# pybabel.exe compile -d translations


from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'pt_BR'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

def get_locale():
    lang = request.cookies.get('language')
    if lang in ['en', 'es', 'pt_BR']:
        return lang
    return request.accept_languages.best_match(['en', 'es', 'pt_BR'])

babel = Babel(app, locale_selector=get_locale)

@app.context_processor
def inject_locale():
    return {'get_locale': get_locale}

@app.route('/')
def hello():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
