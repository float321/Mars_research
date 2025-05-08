from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def slogan():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    text = '''Человечество вырастает из детства.
    Человечеству мала одна планета.
    Мы сделаем обитаемыми безжизненные пока планеты.
    И начнем с Марса!
    Присоединяйся!'''
    return '<br>'.join(text.split('\n'))


@app.route('/image_mars')
def image_mars():
    return f'''
    <html>
        <head>
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='mars.jpg')}" alt="Марс">
            <p><b>Вот она какая, красная планета.</b></p>
        </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
