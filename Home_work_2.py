# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя, 
# а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», 
# при нажатии на которую будет удалён cookie-файл с данными пользователя и 
# произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask,render_template,request,redirect,url_for,make_response
from pathlib import PurePath, Path

app = Flask(__name__)


#отсюда идем
@app.route('/mail/', methods=['GET', 'POST'])
def mail_cook():
    if request.method == 'POST':
        name=request.form.get('name')
        mail=request.form.get('mail')
        response = make_response(render_template('HW_mail.html'))
        response.set_cookie(key='name',value='name',max_age=0)
        return response
 #      return redirect(url_for('set_cookie',name=name)) #redirect для перенаправления на hello
    return render_template('HW_mail.html')

#с сервера
@app.route('/set', methods=['GET', 'POST'])
def set_cookie():
    if request.method=='POST':
        name=request.form.get('name')
        response = make_response(render_template('HW_mail_2.html',name=name)) #объект ответа
        response.set_cookie(key='name',value=name)
        return response
    return redirect(url_for('mail_cook'))



if __name__ == '__main__':
    app.run(debug=False)