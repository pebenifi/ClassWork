from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lines = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(lines)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <img src={url_for('static', filename='img/mars.png')}>
                    <p>Вот она какая, красная планета!</p>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    print(nickname, level, rating)
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                     <title>Результаты отбора</title>
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                  </head>
                  <body>
                    <h1>Результаты отбора!</h1>
                    <p class="alert alert-primary" role="alert">Претендента на участие {nickname}:</p>
                    <p class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</p>
                    <p class="alert alert-secondary" role="alert">составляет {rating}!</p>
                    <p class="alert alert-danger" role="alert">Желаем удачи!</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
