# FLASK INTERNACIONALIZATION

App Flask simples para escolher o idioma do site.

# Requisitos
pip install Flask-Babel

pip install Flask

Comandos para gerar os scripts de tradução:

1. Localizar as strings que deverão ser traduzidas automaticamente. As strings são indicadas no python por _('String'), e nos templates por {{ _('Hello, World!') }}
````commandline
pybabel.exe extract -F babel.cfg -o messages.pot .
````

 2. Criar os arquivos individuais para cada idioma com o comando:

````commandline
pybabel.exe init -i .\messages.pot -d translations -l es
````
Não esquecer de efetuar a tradução no arquivo. Ex:

````html
#: templates/base.html:2
msgid "Heading"
msgstr "Cabeçalho"
````

3. Compilar os arquivos de idioma para serem usados na aplicação:

````commandline
pybabel.exe compile -d translations
````
