from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def motto():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    lines = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(lines)


@app.route('/image_mars')
def mars_with_image():
    html_page = f"""<!doctype html>
                     <html lang="en">
                       <head>
                         <meta charset="utf-8">
                         <title>Привет, Марс!</title>
                       </head>
                       <body>
                         <h1>Жди нас, Марс!</h1>
                         <img src={url_for('static', filename='img/mars.png')}>
                         <p>Вот она какая, красная планета</p>
                       </body>
                      </html>"""
    return html_page


@app.route('/promotion_image')
def promotion_image():
    html_page = f"""<!doctype html>
                        <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                                <title>Привет, Марс!</title>
                            </head>
                            <body>
                                <h1>Жди нас, Марс!</h1>
                                <img src={url_for('static', filename='img/mars.png')}>
                                <p class='alert alert-primary' role='alert'>Человечество вырастает из детства.</p>
                                <p class='alert alert-secondary' role='alert'>Человечеству мала одна планета.</p>
                                <p class='alert alert-success' role='alert'>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                                <p class='alert alert-danger' role='alert'>И начнем с Марса!</p>
                                <p class='alert alert-warning' role='alert'>Присоединяйся!</p>
                            </body>
                        </html>"""
    return html_page


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета Претендета</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input type="text" class="form-control" id="surname" placeholder="Фамилия" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Среднее Профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof1">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof2">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof3">
                                        <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof4">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof5">
                                        <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof6">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof7">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли Вы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
