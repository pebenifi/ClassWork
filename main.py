from flask import Flask, url_for

app = Flask(__name__)
@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def motto():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promo():
    return '<br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                        'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'])


@app.route('/image')
def image():
    return f'''<!doctype html>
                    <html lang="en"
                     <head>
                      <meta charset="utf-8">
                       <title>Привет, Марс</title>
                     </head>
                     <body>
                       <h1>Миссия Колонизация Марса</h1>
                       <img src={url_for('static', filename='images.jpg')}
                        alt="Картинка не найдена">
                        <p>Вот она какая, красная планета!</p>
                     </body>
                    </html>'''
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')